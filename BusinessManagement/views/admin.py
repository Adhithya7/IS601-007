import io
import csv
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    # UCID: ap2823
    # Date: 12/04/2022
    # Method to import csv     
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', "warning")
            return redirect(request.url)
        # TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not
        if file and secure_filename(file.filename):
            if not file.filename.endswith(".csv"):
                flash("Selected file is not a csv file", "danger")
                return redirect(request.url)
            companies = []
            employees = []
            company_query = """
            INSERT INTO IS601_MP2_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE address = %(address)s, city = %(city)s, country=%(country)s, state=%(state)s, zip=%(zip)s, website=%(website)s 
            """
            employee_query = """
             INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1))
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, last_name = %(last_name)s, email = %(email)s, company_id = (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            # TODO importcsv-2 read the csv file stream as a dict
            # UCID: ap2823
            # Date: 12/04/2022
            # Reading csv as dict and processing it
            for row in csv.DictReader(stream, delimiter=','):
                # print(row) #example
                # TODO importcsv-3 extract company data and append to company list as a dict only with company data
                if row["company_name"] and row["address"] and row["city"] and row["state"] and row["zip"] and row["web"] and row["country"]:
                    companies.append({"name": row["company_name"],
                                      "address": row["address"],
                                      "city": row["city"],
                                      "country": row["country"],
                                      "state": row["state"],
                                      "zip": row["zip"],
                                      "website": row["web"]})
                # TODO importcsv-4 extract employee data and append to employee list as a dict only with employee data
                if row["first_name"] and row["last_name"] and row["email"]:
                    employees.append({"first_name": row["first_name"],
                                      "last_name": row["last_name"],
                                      "email": row["email"],
                                      "company_name": row.get("company_name", None)})
               
            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    # TODO importcsv-5 display flash message about number of companies inserted
                    flash(f"Inserted {len(companies)} companies", "success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-6 display flash message (info) that no companies were loaded
                flash("No Companies were inserted", "success")
                pass
            if len(employees) > 0:
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    flash(f"Inserted {len(employees)} employees", "success")
                    # TODO importcsv-7 display flash message about number of employees loaded
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                 # TODO importcsv-8 display flash message (info) that no companies were loaded
                flash("No employees were inserted", "success")
                pass
    return render_template("upload.html")
