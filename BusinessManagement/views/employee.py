import traceback as tb
from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
from views.forms import *
import copy
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    # UCID: ap2823
    # Date: 12/04/2022
    # Method to search employee using request args
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = """ SELECT A.id, first_name, last_name, email, company_id, IF(name is not null, name,'N/A') as company_name FROM IS601_MP2_Employees A
                LEFT JOIN IS601_MP2_Companies B on A.company_id=B.id
                WHERE 1=1"""
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    # TODO search-3 append like filter for first_name if provided
    # TODO search-4 append like filter for last_name if provided
    # TODO search-5 append like filter for email if provided
    # TODO search-6 append equality filter for company_id if provided
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    filters = [("fn", "first_name"), ("ln", "last_name"), ("email", "email")]
    for filter_arg,filter in filters:
        if request.args.get(filter_arg):
            query += f" and {filter} like %s"
            args.append(f"%{request.args.get(filter_arg)}%")
    if request.args.get("company"):
        query += f" and company_id = %s"
        args.append(request.args.get('company'))
    if request.args.get("order") and request.args.get("column"):
        if request.args.get("column") in allowed_columns \
            and request.args.get("order") in ["asc", "desc"]:
            query += f" ORDER BY {request.args.get('column')} {request.args.get('order')}"
    query += f" LIMIT %s"
    ql = int(request.args.get('limit', 10))
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
            print(rows)
    except Exception as e:
        # TODO search-10 make message user friendly
        print(tb.format_exc)
        flash(f"Unexpected error while trying to search employee: {e}", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    allowed_columns = [(col,col) for col in allowed_columns]
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    # UCID: ap2823
    # Date: 12/04/2022
    # Method to add employee using WT-Forms
    form = Employee(request.form)
    if request.method == "POST":
        form_data = {}
        field_missing = False
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        # if not form.validate_on_submit():
        #     return render_template("add_employee.html", form=form)
        form_data["first_name"] = form.first_name.data
        form_data["last_name"] = form.last_name.data
        form_data["company"] = request.form.get("company") or None
        form_data["email"] = form.email.data
        for k,v in form_data.items():
            if k != "company" and not v:
                flash(f"{k} is a mandatory field", "danger")
                field_missing = True
        if not field_missing:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP2_Employees (first_name, last_name, company_id, email)
                VALUES (%s, %s, %s, %s)
                """, *form_data.values()
                ) # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                print(tb.format_exc)
                flash(f"Unexpected error while trying to add employee: {e}", "danger")
    return render_template("add_employee.html", form=form)

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # UCID: ap2823
    # Date: 12/04/2022
    # Method to edit employee using request args and WTforms
    # TODO edit-1 request args id is required (flash proper error message)
    row = None
    form = Employee(request.form)
    if request.args.get('id'): # TODO update this for TODO edit-1
        if request.method == "POST":
            form_data = {}
            field_missing = False
            # if not form.validate_on_submit():
            #     return render_template("edit_employee.html", form=form)
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            # TODO edit-2 first_name is required (flash proper error message)
            # TODO edit-3 last_name is required (flash proper error message)
            # TODO edit-4 company may be None
            # TODO edit-5 email is required (flash proper error message)
            form_data["first_name"] = form.first_name.data
            form_data["last_name"] = form.last_name.data
            form_data["company"] = request.form.get("company") or None
            form_data["email"] = form.email.data
            form_data["id"] = request.args.get('id')
            for k,v in form_data.items():
                if k != "company" and not v:
                    flash(f"{k} is a mandatory field", "danger")
                    field_missing = True
            if not field_missing:
                try:
                    # TODO edit-6 fill in proper update query
                    result = DB.update("""
                    UPDATE IS601_MP2_Employees 
                    SET first_name=%s, last_name=%s, company_id=%s, email=%s
                    WHERE id=%s
                    """, *form_data.values())
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    print(tb.format_exc)
                    # TODO edit-7 make this user-friendly
                    flash(f"Unexpected error while trying to edit employee: {e}", "danger")
        try:
            # TODO edit-8 fetch the updated data (including company_name)
            # company_name should be 'N/A' if the employee isn't assigned to a copany
            result = DB.selectOne("""
            SELECT * FROM IS601_MP2_Employees A
            LEFT JOIN IS601_MP2_Companies B on A.company_id=B.id
            WHERE A.id = %s
            """, request.args.get('id'))
            if result.status:
                row = result.row
                form.first_name.data = row["first_name"]
                form.last_name.data = row["last_name"]
                form.email.data = row["email"]
        except Exception as e:
            print(tb.format_exc())
            # TODO edit-9 make this user-friendly
            flash(f"Unexpected error while trying to fetch the updated employee: {e}", "danger")
    else:
        flash("Employee ID is missing", "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", form=form, company=row.get("company_id"))

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # UCID: ap2823
    # Date: 12/04/2022
    # Method to delete employee using employee_id and then redirect to listing page
    if request.method == "GET":
        emp_id = request.args.get("id")
        if not emp_id:
            flash("Employee ID is missing", "danger")
            return render_template("list_employees.html")
        try:
            result = DB.delete("""
            DELETE FROM IS601_MP2_Employees
            WHERE id = %s
            """, emp_id)
            if result.status:
                flash("Deleted Record", "success")
        except Exception as e:
            flash(f"Unexpected error while trying to delete the employee: {e}", "danger")
        new_args = dict(request.args)
        del new_args["id"]
    return redirect(url_for("employee.search", **new_args))
