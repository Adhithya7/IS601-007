import traceback as tb
from flask import Blueprint, render_template, flash, redirect, url_for,current_app, session
from auth.forms import RegisterForm, LoginForm
from sql.db import DB

from flask_login import login_user, login_required, logout_user, current_user
from auth.models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

from flask_principal import Identity, AnonymousIdentity, \
     identity_changed

auth = Blueprint('auth', __name__, url_prefix='/',template_folder='templates')

def check_duplicate(e):
    import re
    r = re.match(".*IS601_Users.(\w+)", str(e))
    if r:
        flash(f"The chosen {r.group(1   )} is not available", "warning")
    else:
        flash("Unknown error occurred, please try again", "danger")
        print(tb.format_exc())



@auth.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    # wtform validators are both client-side and server-side
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        username = form.username.data
        try:
            hash = bcrypt.generate_password_hash(password)
            # save the hash, not the plaintext password
            result = DB.insertOne("INSERT INTO IS601_Users (email, username, password) VALUES (%s, %s, %s)", email, username, hash)
            if result.status:
                flash("Successfully registered","success")
        except Exception as e:
            check_duplicate(e)
    return render_template("register.html", form=form)

@auth.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        is_valid = True
        email = form.email.data # email or username
        password = form.password.data
        if is_valid:
            try:
                result = DB.selectOne("SELECT id, email, username, password FROM IS601_Users where email= %(email)s or username=%(email)s", {"email":email})
                if result.status and result.row:
                    hash = result.row["password"]
                    if bcrypt.check_password_hash(hash, password):
                        del result.row["password"] # don't carry password/hash beyond here
                        user = User(**result.row)
                        success = login_user(user) # login the user via flask_login
                        
                        if success:
                            # Tell Flask-Principal the identity changed
                            identity_changed.send(current_app._get_current_object(),
                                    identity=Identity(user.id))
                            # store user object in session as json
                            session["user"] = user.toJson()
                            flash("Log in successful", "success")
                            return redirect(url_for("auth.landing_page"))
                        else:
                            flash("Error logging in", "danger")
                else:
                    # invalid user and invalid password together is too much info for a potential attacker
                    # normally we return a single message for both "invalid username or password" so an attacker doens't know which part was correct
                    flash("Invalid username or password", "warning")

            except Exception as e:
                flash(str(e), "danger")
    return render_template("login.html", form=form)

@auth.route("/logout", methods=["GET"])
def logout():
    logout_user()
     # Remove session keys set by Flask-Principal
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)

    # Tell Flask-Principal the user is anonymous
    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())
    flash("Successfully logged out", "success")
    return redirect(url_for("auth.login"))

@auth.route("/profile", methods=["GET","POST"])
def profile():
    pass

@auth.route("/landing-page", methods=["GET","POST"])
@login_required
def landing_page():
    return render_template("landing_page.html")