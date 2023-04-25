class ProductController:
    def __init__(self):
        self.products =[
            {
                "title":"Minimalis Chair",
                "description":"Sleek, stylish, and minimalist chairs.",
                "price":450,
                "image":"/static/product/product-1.jpg"
            },
            {
                "title":"Family Sofa",
                "description":"Comfortable, cozy, and perfect for families.",
                "price":800,
                "image":"/static/product/product-2.jpg"
            },
            {
                "title":"Cupboard",
                "description":"Stylish, functional, and space-saving cupboards.",
                "price":660,
                "image":"/static/product/product-3.jpg"
            },
            {
                "title":"Arabic Lamp",
                "description":"Exquisite, intricate, and stunning Arabic lamps.",
                "price":3500,
                "image":"/static/product/product-4.jpg"
            },
            {
                "title":"Ancient Cupboard",
                "description":"Historic, distinctive, and charming Ancient Cupboard.",
                "price":780,
                "image":"/static/product/product-5.jpg"
            },
            {
                "title":"Minimalis Table",
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

