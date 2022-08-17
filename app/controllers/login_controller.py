from flask import render_template, make_response, redirect


def show_login():
    action_url = "/loginuser"
    return render_template("login.html", action_url=action_url)


def login_user(request):
    # set a cookie with user name
    name = request.form.get("name")
    resp = make_response(redirect("/viewcart"))
    resp.set_cookie(
        key="userid",
        value=name,
        samesite="None",
        secure=True,
        httponly=True,
    )
    return resp


def logout_user():
    resp = make_response(render_template("index.html"))
    resp.delete_cookie("userid")
    return resp
