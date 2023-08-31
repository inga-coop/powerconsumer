from flask import Flask, render_template, request
from services.api_service import APIService
from services.data_service import DataService

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("base.html")


# Update the search view method
@app.route("/search", methods=["GET", "POST"])
def search():
    # If the form is submitted
    if request.method == "POST":
        query = request.form["query"]
        product_list = APIService.get_product_data(query)
        return render_template("product_list.html", product_list=product_list)
    # In case of a GET request or any other
    return render_template("search.html")


@app.route("/product-list", methods=["GET"])
def product_list():
    page = request.args.get("page", 1, type=int)
    product_list, next_url, prev_url = APIService.paginator("", page, 10)
    return render_template(
        "product_list.html",
        product_list=product_list,
        next_url=next_url,
        prev_url=prev_url,
    )


@app.route("/product-list/<int:page>")
def product_list_page(page):
    product_list, next_url, prev_url = APIService.paginator("", page, 10)
    return render_template(
        "product_list.html",
        product_list=product_list,
        next_url=next_url,
        prev_url=prev_url,
    )


@app.route("/product-detail/<product_id>", methods=["GET"])
def product_detail(product_id):
    # Fetch product detail from service
    product = APIService.get_product_data(product_id)
    company = APIService.get_company_data(product["company_id"])

    # Render product detail page with the data
    return render_template("product_detail.html", product=product, company=company)


if __name__ == "__main__":
    app.run()
