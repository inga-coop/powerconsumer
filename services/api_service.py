class APIService:
    def get_product_data(product_name):
        return [
            [
                "https://www.drogariaminasbrasil.com.br/media/product/38d/biscoito-recheado-bono-chocolate-126g-nestle-510.jpg",
                product_name,
                "c1",
            ],
            [
                "https://tfdfn2.vtexassets.com/arquivos/ids/218879/biscoito-aymore-maizena-170g.png?v=638168145698870000",
                product_name,
                "c2",
            ],
        ]

    def get_company_data(company_name):
        # API call to get company data
        pass

    def paginator(query, page, per_page):
        products = APIService.get_product_data(query)
        items = products.items[per_page * (page - 1) : per_page * page]
        has_next = True if len(products.items) > per_page * page else False
        has_prev = True if page > 1 else False
        return items, has_next, has_prev
