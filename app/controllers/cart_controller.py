from flask import render_template


def update_cart(request):
    # Get name from cookie
    name = request.cookies.get("userid")
    item = request.form.get("items")
    count = request.form.get("count")
    print(f"update_car name: {name} item: {item}, count: {count}")
    return render_template("cart.html", action_url="/updatecart", name=name)
