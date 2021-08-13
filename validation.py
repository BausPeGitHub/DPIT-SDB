from exceptions import ValidationError
import datetime

class ProductValidator :
    def __init__(self) :
        super().__init__()
    def code_validator(self , code) :
        if len(code) > 10 :
            raise ValidationError("Invalid product code")
        try :
            for digit in code :
                int_digit = int(digit)
        except Exception :
            raise ValidationError("Invalid product code")
    def price_validator(self , price) :
        try :
            float_price = float(price)
        except Exception :
            raise ValidationError("Price must be a real number")
    def quantity_validator(self , quantity) :
        try :
            int_quantity = int(quantity)
        except Exception :
            raise ValidationError("Quantity must be a real number")
            
class PromotionValidator :
    def __init__(self) :
        super().__init__()
    def value_validator(self , value) :
        try :
            float_price = float(value)
        except Exception :
            raise ValidationError("Invalid promotion value")
        if 0 > float(value) or float(value) > 100 :
            raise ValidationError("Invalid promotion value")
    def expiration_date_validator(self , date) :
        pattern = "%d-%m-%Y"
        try :
            if date != datetime.datetime.strptime(date , pattern).strftime(pattern) :
                raise ValueError
        except ValueError :
            raise ValidationError("Invalid expiration date")