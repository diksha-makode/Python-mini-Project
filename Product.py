'''Car showroom management system'''
class Product:
    def __init__(self,product_id,p_name,p_price,p_quantity,p_description):
        self.product_id = product_id
        self.product_name=p_name
        self.product_price=p_price
        self.product_quantity=p_quantity
        self.product_description=p_description


    def __str__(self):
        return str(self.product_id) + ","+ self.product_name + ","+ str(self.product_price) + ","+ str(self.product_quantity ) + ","+self.product_description + "\n"


