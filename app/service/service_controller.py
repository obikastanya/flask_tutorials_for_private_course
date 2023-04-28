import traceback

class ServiceKindController:
    def __init__(self):
        self._service_kinds=[
            {
                "id":"1",
                "title":"4 Chair and 2 Minimalis Table",
                "price":3200
            },
            {
                "id":"2",
                "title":"1 Family Sofa and 1 Minimalis Table",
                "price":950
            },
            {
                "id":"3",
                "title":"Minimalis Chair",
                "price":450
            },
            {
                "id":"4",
                "title":"Family Sofa",
                "price":800
            },
            {
                "id":"5",
                "title":"Arabic Lamp",
                "price":3500
            },
            {
                "id":"6",
                "title":"CupBoard",
                "price":660
            },
            {
                "id":"7",
                "title":"Ancient Cupboard",
                "price":780
            },
            {
                "id":"8",
                "title":"Minimalis Table",
                "price":480
            }
        ]
    
    def get_service_kinds(self):
        return self._service_kinds
    
    def get_service_kind_by_id(self, id):
        for service_kind in self._service_kinds:
            if service_kind.get("id") == id:
                return service_kind
        



class ServiceController:
    def __init__(self):
        self.service_kind = ServiceKindController()
        self.insurance_price = 0.8/100
        self.installation_support_fee = 50
        self.shipping_price = {
            "indonesia":80,
            "international":160
        }
    
    def calculate_price_estimation(
            self, 
            service_kind_id,
            amount,
            insurance,
            installation_support,
            shipping
        ):
        
        try:
            amount = int(amount)
            service_kind = self.service_kind.get_service_kind_by_id(service_kind_id)
            
            service_kind_price = service_kind.get("price")
            total_product_price = service_kind_price * amount
            shipping_price = self.shipping_price.get(shipping)
            
            installation_fee = 0
            if installation_support == "yes":
                installation_fee = self.installation_support_fee
            
            insurance_price = 0
            if insurance == "yes":
                insurance_price = self.insurance_price * total_product_price

            total_price =  (
                total_product_price 
                + insurance_price
                + installation_fee
                + shipping_price
                )
            return int(total_price)
        except:
            traceback.print_exc()
            return 0

    
    
    
