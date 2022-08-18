from flask import render_template, redirect

from app.utility import redis_conn


def view_cart(request, error_msg):
    user_id = request.cookies.get("userid")
    print(f"view_cart user_id: {user_id}")
    if not user_id:
        return redirect("/login")

    items = redis_conn.hgetall(f"cart:{user_id}")

    for key, value in items.items():
        print(key, '->', value)

    return render_template("cart.html", action_url="/updatecart", name=user_id, items=items, error_msg=error_msg)


def update_cart(request):
    # Get name from cookie
    name = request.cookies.get("userid")
    item = request.form.get("items")
    error_msg = None
    try:
        count = int(request.form.get("count"))
        if count == 0:
            redis_conn.hdel(f"cart:{name}", item)
        else:
            redis_conn.hset(f"cart:{name}", mapping={item: count})
    except:
        count = request.form.get("count")
        error_msg = f"Invalid count: {count}"

    print(f"update_cart name: {name} item: {item}, count: {count}")

    return view_cart(request, error_msg=error_msg)
