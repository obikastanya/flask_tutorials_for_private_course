class OurClientController:
    def __init__(self):
        self._clients =[
            {"name":"Meikarta"},
            {"name":"Ciputra"},
            {"name":"Pulman"},
            {"name":"Wahid"}
        ]

    def get_clients(self):
        return self._clients


class OurServiceContoller:
    def __init__(self):
        self._service_description ="""
        Our interior industry service specializes in creating stunning and functional spaces that reflect your personal style. 
        Our team of designers, architects, project managers, and craftsmen work together to provide a customized design plan that 
        fits your unique needs and budget. From concept to completion, 
        we ensure exceptional customer service and high-quality standards. 
        """
    
    def get_service(self):
        return self._service_description
    
class AboutUsController:
    def __init__(self):
        self._full_desc = """
        We create stunning and functional environments for homes, offices, and commercial spaces. Our team of designers, architects, project managers, 
        and craftsmen work closely with you to create a customized design plan that reflects your personal style and needs. 
        We are committed to exceptional customer service and building strong relationships with our clients. 
        Contact us today to transform your space into a beautiful and functional environment.
        """
        self.short_desc = """
        We design beautiful and functional spaces for homes, offices, and commercial properties. 
        Contact us to transform your space today.
        """
    
    def get_description(self):
        data = {
            "short_desc":self.short_desc,
            "full_desc":self._full_desc
        }
        return data
    
class HomeController:
    def __init__(self):
        self.client = OurClientController()
        self.service = OurServiceContoller()
        self.about_us = AboutUsController()

    def get_home_page_data(self):
        data = {
            "clients":self.client.get_clients(),
            "service": self.service.get_service(),
            "about_us":self.about_us.get_description()
        }
        return data
