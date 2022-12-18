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

@shop.route("/shop/item", methods=["GET","POST"])
@login_required
def shop_item():
    # UCID: ap2823
    # Date: 12/17/2022
    # Method to view item as a logged-in user
    try:
        id = request.args.get("id" or None)
        result = DB.selectOne("SELECT id, name, description, stock, unit_price, image FROM IS601_S_Items WHERE id = %s", id)
        if result.status and result.row:
            rows = result.row
    except Exception as e:
        print("Error fetching item", e)
        flash("Item not found", "danger")
        rows = []
    return render_template("view_item.html", rows=rows)

@shop.route("/cart", methods=["GET","POST"])
@login_required
def cart():
    # UCID: ap2823
    # Date: 12/17/2022
    # Method to add item to a cart as a logged-in user
    item_id = request.form.get("item_id")
    id = request.form.get("id", item_id)
    print("id", id)
    quantity = request.form.get("quantity", 1, type=int)
    user_id = current_user.get_id()
    if id and user_id:
        if quantity > 0:
            try:
                result = DB.selectOne("SELECT unit_price,name,stock from IS601_S_Items WHERE id = %s", id)
                print("result", result)
                if result.status and result.row:
                    unit_price = result.row["unit_price"]
                    name = result.row["name"]
                    stock = result.row["stock"]
                    if quantity > stock:
                        flash(f"{quantity} {name}s are not available; Please reduce the quantity", "danger")
                    else:
                        if item_id: # update from cart
                            result = DB.insertOne("""
                            UPDATE IS601_S_Cart SET
                            quantity = %(quantity)s,
                            unit_price = %(unit_price)s
                            WHERE item_id = %(id)s and user_id = %(user_id)s
                            """,{
                                "id":id,
                                "quantity": quantity,
                                "unit_price":unit_price,
                                "user_id":user_id
                            })
                            if result.status:
                                flash(f"Updated quantity for {name} to {quantity}", "success")
                        else: #add from shop
                            result = DB.insertOne("""
                            INSERT INTO IS601_S_Cart (item_id, quantity, unit_price, user_id)
                            VALUES(%(id)s, %(quantity)s, %(unit_price)s, %(user_id)s)
                            ON DUPLICATE KEY UPDATE
                            quantity = quantity + %(quantity)s,
                            unit_price = %(unit_price)s
                            """,{
                                "id":id,
                                "quantity": quantity,
                                "unit_price":unit_price,
                                "user_id":user_id
                            })
                            if result.status:
                                flash(f"Added {quantity} of {name} to cart", "success")
            except Exception as e:
                print("Error updating cart" ,e)
                flash("Error updating cart", "danger")
        else:
            # assuming delete
            try:
                result = DB.delete("DELETE FROM IS601_S_Cart where item_id = %s and user_id = %s", id, user_id)
                if result.status:
                    flash("Deleted item from cart", "success")
            except Exception as e:
                print("Error deleting item", e)
                flash("Error deleting item from cart", "danger")
    rows = []
    try:
        result = DB.selectAll("""SELECT c.id, item_id, name, c.quantity, (c.quantity * c.unit_price) as subtotal 
        FROM IS601_S_Cart c JOIN IS601_S_Items i on c.item_id = i.id
        WHERE c.user_id = %s
        """, current_user.get_id())
        if result and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting cart", e)
        flash("Error fetching cart", "danger")
    return render_template("cart.html", rows=rows)