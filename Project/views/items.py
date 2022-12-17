from flask import Blueprint, request, flash, render_template, redirect, url_for
from werkzeug.datastructures import MultiDict
from sql.db import DB
from flask_login import login_required, current_user
import traceback as tb
shop = Blueprint('shop', __name__, url_prefix='/',template_folder='templates')

@shop.route("/shop", methods=["GET","POST"])
@login_required
def shop_list():
    # UCID: ap2823
    # Date: 12/17/2022
    # Method to view item as a logged-in user
    rows = []
    query = """SELECT id, name, description, stock, unit_price, image
               FROM IS601_S_Items WHERE visibility = 1"""
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["name", "description", "unit_price"]
    for filter in allowed_columns[:-1]:
        if request.args.get(filter):
            query += f" and {filter} like %s"
            args.append(f"%{request.args.get(filter)}%")
    if request.args.get("order") and request.args.get("column"):
        if request.args.get("column") in allowed_columns \
            and request.args.get("order") in ["asc", "desc"]:
            query += f" ORDER BY {request.args.get('column')} {request.args.get('order')}"
    query += f" LIMIT %s"
    ql = int(request.args.get('limit', 25))
    if ql < 1 or ql > 100:
        flash("limit value should be in the range of 1-100; Defaulting to 25")
        args.append(25)
    else:
        args.append(ql)
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(tb.format_exc())
        flash("There was a problem loading items", "danger")
    return render_template("shop.html", rows=rows, allowed_columns=allowed_columns)