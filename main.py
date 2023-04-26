from flask import (
    Flask, 
    render_template,
    request,
    redirect,
    make_response
)

from app.home.home_controller import HomeController
from app.product.product_controller import ProductController
from app.award.award_controller import AwardController
from app.service.service_controller import ServiceController
from app.login.login_controller import LoginController


home_controller = HomeController()
product_controller = ProductController()
award_controller = AwardController()
service_controller = ServiceController()
login_controller = LoginController()

app = Flask(__name__)

@app.get("/login")
def login():
    if request.cookies.get("user"):
        return redirect("/")
    return render_template("login.html")


@app.get("/logout")
def logout():
    if not request.cookies.get("user"):
        return redirect("/login")
    response = make_response ( redirect("/login") )
    response.delete_cookie("user")
    return response
    

@app.post("/login")
def login_post():
    
    email = request.form.get("email")
    password = request.form.get("password")
    result = login_controller.login(email, password)

    login_status = result[0]
    error_message = result[1]
    user = result[2]

    if login_status:
        response = make_response( redirect("/") )
        user_email = user.get("email")
        response.set_cookie("user", user_email)
        return response
    
    return render_template("login.html", error_message=error_message)


@app.get("/")
def home():
    if not request.cookies.get("user"):
        return redirect("/login")
    data = home_controller.get_home_page_data()
    user = request.cookies.get("user")
    return render_template(
        "index.html", 
        clients = data.get("clients"), 
        about_us = data.get('about_us') ,
        service = data.get("service"),
        user = user
    )


@app.get("/product")
def product():
    if not request.cookies.get("user"):
        return redirect("/login")
    products = product_controller.get_products()
    user = request.cookies.get("user")
    return render_template("product.html", products = products, user = user)


@app.get("/product/<product_id>/")
def product_detail(product_id):
    if not request.cookies.get("user"):
        return redirect("/login")
    product = product_controller.get_product_by_id(product_id)
    user = request.cookies.get("user")
    return render_template("product_detail.html", product = product, user = user)

@app.get("/award")
def award():
    if not request.cookies.get("user"):
        return redirect("/login")
    awards = award_controller.get_awards()
    user = request.cookies.get("user")
    return render_template("award.html", awards = awards, user = user)

@app.get("/service")
def service_get():
    if not request.cookies.get("user"):
        return redirect("/login")
    service_kinds = service_controller.service_kind.get_service_kinds()
    user = request.cookies.get("user")
    return render_template("service.html", service_kinds = service_kinds, user = user)

@app.post("/service")
def service_post():
    if not request.cookies.get("user"):
        return redirect("/login")
    service_kind_id = request.form.get("service_kind")
    amount = request.form.get("amount")
    insurance = request.form.get("insurance")
    installation_support = request.form.get("installation_support")
    shipping = request.form.get("shipping")
    user = request.cookies.get("user")

    price_estimation = service_controller.calculate_price_estimation(
        service_kind_id,
        amount,
        insurance,
        installation_support,
        shipping
    )

    service_kinds = service_controller.service_kind.get_service_kinds()
    return render_template(
        "service.html", 
        service_kinds = service_kinds,
        price_estimation = price_estimation,
        service_kind_id = service_kind_id,
        amount = amount,
        insurance = insurance,
        installation_support = installation_support,
        shipping = shipping, 
        user = user
    )


if __name__ == "__main__":
    # localhost ==  "127.0.0.1"
    app.run(host="127.0.0.1", port=8080, debug=True)

