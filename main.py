from flask import Flask
from flask import render_template
from flask import request

from app.home.home_controller import HomeController
from app.product.product_controller import ProductController
from app.award.award_controller import AwardController
from app.service.service_controller import ServiceController

home_controller = HomeController()
product_controller = ProductController()
award_controller = AwardController()
service_controller = ServiceController()

app = Flask(__name__)


@app.get("/")
def home():
    data = home_controller.get_home_page_data()
    return render_template(
        "index.html", 
        clients = data.get("clients"), 
        about_us = data.get('about_us') ,
        service = data.get("service")
    )

@app.get("/product")
def product():
    products = product_controller.get_products()
    return render_template("product.html", products = products)


@app.get("/product/<product_id>/")
def product_detail(product_id):
    product = product_controller.get_product_by_id(product_id)
    return render_template("product_detail.html", product = product)

@app.get("/award")
def award():
    awards = award_controller.get_awards()
    return render_template("award.html", awards = awards)

@app.get("/service")
def service_get():
    service_kinds = service_controller.service_kind.get_service_kinds()
    return render_template("service.html", service_kinds = service_kinds)

@app.post("/service")
def service_post():
    
    service_kind_id = request.form.get("service_kind")
    amount = request.form.get("amount")
    insurance = request.form.get("insurance")
    installation_support = request.form.get("installation_support")
    shipping = request.form.get("shipping")

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
        shipping = shipping
    )


if __name__ == "__main__":
    # localhost ==  "127.0.0.1"
    app.run(host="127.0.0.1", port=8080, debug=True)