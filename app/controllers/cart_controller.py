from flask import render_template

from app.utility import redis_conn


def update_cart(request):
    # Get name from cookie
    name = request.cookies.get("userid")
    item = request.form.get("items")
    count = int(request.form.get("count"))
    print(f"update_cart name: {name} item: {item}, count: {count}")
    if not count or count <= 0:
        redis_conn.hrem(f"cart:{name}")
    else:
        redis_conn.hset(f"cart:{name}", item, count)

    return render_template("cart.html", action_url="/updatecart", name=name)
