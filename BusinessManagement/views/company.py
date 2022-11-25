import traceback as tb
from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
from forms import *
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count for the company
    # don't do SELECT *
    query = """SELECT id, name, address, city, country, state, zip, website,
               (SELECT count(*) from IS601_MP2_Employees A
                WHERE A.company = B.id) AS employee_count
               FROM IS601_MP2_Companies B
               WHERE 1=1"""
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    # TODO search-3 append a LIKE filter for name if provided
    # TODO search-4 append an equality filter for country if provided
    # TODO search-5 append an equality filter for state if provided
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    filters = ["country", "state"]
    if request.args.get("name"):
        query += " and name like %s"
        args.append(f"%{request.args.get('name')}%")
    for filter in filters:
        if request.args.get(filter):
            query += f" and {filter} = %s"
            args.append(request.args.get(filter))
    if request.args.get("order") and request.args.get("column"):
        if request.args.get("column") in allowed_columns \
            and request.args.get("order") in ["asc", "desc"]:
            query += f" ORDER BY %s %s"
            args.append(request.args.get('column'))
            args.append(request.args.get('order'))
    query += f" LIMIT %s"
    ql = request.args.get('limit', 10)
    if ql < 1 or ql > 100:
        flash("limit value should be in the range of 1-100; Defaulting to 10")
        args.append(10)
    else:
        args.append(ql)
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        print(tb.format_exc)
        flash(f"Unexpected error while trying to search company: {e}", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        form = Company()
        form_data = {}
        has_error = False
        if not form.validate_on_submit():
            return render_template("add_company.html", form=form)
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-6 country is required (flash proper error message)
        # TODO add-7 website is not required
        form_data["name"] = form.name.data
        form_data["address"] = form.address.data
        form_data["city"] = form.city.data
        form_data["country"] = request.form.get("country")
        form_data["state"] = request.form.get("state")
        form_data["zip_code"] = form.zip_code.data
        form_data["website"] = form.website.data
        for k,v in form_data.items():
            if k != "website" and not v:
                flash(f"{k} is a mandatory field", "danger")
                has_error = True
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP2_Companies (name, address, city, country,
                state, zip_code, website)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, *form_data.values()
                ) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                print(tb.format_exc)
                flash(f"Unexpected error while trying to add company: {e}", "danger")
    return render_template("add_company.html", form=form)

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    row = None
    if request.args.get('id'): # TODO update this for TODO edit-1
        if request.method == "POST":
            # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-3 name is required (flash proper error message)
            # TODO edit-4 address is required (flash proper error message)
            # TODO edit-5 city is required (flash proper error message)
            # TODO edit-6 state is required (flash proper error message)
            # TODO edit-7 country is required (flash proper error message)
            # TODO edit-8 website is not required
            # 
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            #data = [name, address, city, state, country, zipcode, website]
            form_data = {}
            form = Company()
            has_error = False
            if not form.validate_on_submit():
                return render_template("edit_company.html.html", form=form)
            form_data["name"] = form.name.data
            form_data["address"] = form.address.data
            form_data["city"] = form.city.data
            form_data["country"] = request.form.get("country")
            form_data["state"] = request.form.get("state")
            form_data["zip_code"] = form.zip_code.data
            form_data["website"] = form.website.data
            form_data["id"] = request.args.get('id')
            for k,v in form_data.items():
                if k != "website" and not v:
                    flash(f"{k} is a mandatory field", "danger")
                    has_error = True
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    result = DB.update("""
                    UPDATE IS601_MP2_Companies 
                    SET name=%s, address=%s, city=%s, country=%s, state=%s,
                    zip=%s, website=%s
                    WHERE id=%s
                    """, *form_data.values())
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    print(tb.format_exc)
                    # TODO edit-10 make this user-friendly
                    flash(f"Unexpected error while trying to edit company: {e}", "danger")
                try:
                    # TODO edit-11 fetch the updated data
                    result = DB.selectOne("""SELECT * FROM IS601_MP2_Companies
                    WHERE id=%s""", form_data["id"])
                    if result.status:
                        row = result.row
                except Exception as e:
                    print(tb.format_exc())
                    # TODO edit-12 make this user-friendly
                    flash(f"Unexpected error while trying to fetch the updated company: {e}", "danger")
    else:
        flash("Company ID is missing", "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", form=form)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    if request.method == "GET":
        cmp_id = request.args.get("id")
        if not cmp_id:
            flash("Company ID is missing", "danger")
            return render_template("list_companies.html")
        try:
            constraint_fix = DB.update("""
            UPDATE IS601_MP2_Employees
            SET company = NULL
            WHERE id = %s
            """,cmp_id)

            result = DB.delete("""
            DELETE FROM IS601_MP2_Companies
            WHERE id = %s
            """, cmp_id)

            if constraint_fix.status and result.status:
                flash("Deleted Record", "success")
        except Exception as e:
            flash(f"Unexpected error while trying to delete the Company: {e}", "danger")
        del request.args["id"]
    return redirect(url_for('search'))