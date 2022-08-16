from flask import render_template, make_response


def login_user(request):
    # set a cookie with user name
    name = request.form.get("name")
    resp = make_response(render_template("cart.html", action_url="/updatecart", name=name))
    resp.set_cookie(
        key="userid",
        value=name,
        samesite="None",
        secure=True,
        httponly=True,
    )
    return resp
