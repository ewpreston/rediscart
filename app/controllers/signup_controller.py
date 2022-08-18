import hashlib

from flask import render_template, make_response, redirect

from app.utility import redis_conn


def show_signup():
    action_url = "/signupuser"
    return render_template("signup.html", action_url=action_url)


def signup_user(request):
    # set a cookie with user name
    userid = request.form.get("userid")
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    email = request.form.get("email")
    password = request.form.get("password")

    redis_conn.hset(f"users:{userid}", mapping={"firstname": first_name, "lastname": last_name, "email": email,
                                                "password": hashlib.md5(password.encode()).hexdigest()})

    print(f"signup_user userid: {userid}")
    resp = make_response(redirect("/login"))
    return resp
