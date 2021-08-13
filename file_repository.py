from entities import Product
from validation import ProductValidator
from exceptions import ValidationError

class FileRepository :
    def __init__(self) :
        self.__product_list = []
        self.__product_validator = ProductValidator()
        
    def get_product_list(self) :
        return self.__product_list
    
    def read_product_details(self) :
        with open("products.txt" , "r") as f :
            content = f.readlines()
            for line in content :
                product_info = line.split(" , ")
                if len(product_info) != 5 :
                    raise ValidationError("Invalid product information!")
                self.__product_validator.code_validator(product_info[0])
                self.__product_validator.price_validator(product_info[3])
                self.__product_validator.quantity_validator(product_info[4])
                product = Product(product_info[0] , product_info[1] , product_info[2] , float(product_info[3]) , int(product_info[4]))
                self.__product_list.append(product)
            
