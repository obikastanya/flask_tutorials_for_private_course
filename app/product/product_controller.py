class ProductController:
    def __init__(self):
        self.products =[
            {
                "id":"1",
                "title":"Minimalis Chair",
                "type":"Furniture",
                "description":"Sleek, stylish, and minimalist chairs.",
                "price":450,
                "image":"/static/product/product-1.jpg"
            },
            {
                "id":"2",
                "title":"Family Sofa",
                "type":"Furniture",
                "description":"Comfortable, cozy, and perfect for families.",
                "price":800,
                "image":"/static/product/product-2.jpg"
            },
            {
                "id":"3",
                "title":"Cupboard",
                "type":"Furniture",
                "description":"Stylish, functional, and space-saving cupboards.",
                "price":660,
                "image":"/static/product/product-3.jpg"
            },
            {
                "id":"4",
                "title":"Arabic Lamp",
                "type":"Electronic",
                "description":"Exquisite, intricate, and stunning Arabic lamps.",
                "price":3500,
                "image":"/static/product/product-4.jpg"
            },
            {
                "id":"5",
                "title":"Ancient Cupboard",
                "type":"Electronic",
                "description":"Historic, distinctive, and charming Ancient Cupboard.",
                "price":780,
                "image":"/static/product/product-5.jpg"
            },
            {
                "id":"6",
                "title":"Minimalis Table",
                "type":"Electronic",
                "description":"Contemporary, functional, and stylish minimalist tables.",
                "price":480,
                "image":"/static/product/product-6.jpg"
            }
        ]
    
    def get_products(self):
        data ={
            "section_1":self.products[0:2],
            "section_2":self.products[2:4],
            "section_3":self.products[4:]
        }
        return data
    
    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.get("id") == product_id:
                return product
