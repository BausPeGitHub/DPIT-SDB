class Product :
    def __init__(self , code : str , name : str , firm : str , price : float , quantity : int) :
        self.__code = code
        self.__name = name
        self.__firm = firm
        self.__price = price
        self.__quantity = quantity
        
    def get_code(self) :
        return self.__code
    
    def get_name(self) :
        return self.__name
    
    def get_firm(self) :
        return self.__firm
    
    def get_price(self) :
        return self.__price
    
    def get_quantity(self) :
        return self.__quantity
    
    def set_code(self , new_code) :
        self.__code = new_code
    
    def set_name(self , new_name) :
        self.__name = new_name
    
    def set_firm(self , new_firm) :
        self.__firm = new_firm
    
    def set_price(self , new_price) :
        self.__price = new_price
    
    def set_quantity(self , new_quantity) :
        self.__quantity = new_quantity
    
    def __eq__(self , other) :
        return self.__code == other.get_code()
    
    def __str__(self) :
        return "Code : {0} , Name : {1} , Firm : {2} , Price : {3} , Quantity : {4}". format(self.__code , self.__name , self.__firm , self.__price , self.__quantity)
    
    def __repr__(self) :
        return "Code : {0} , Name : {1} , Firm : {2} , Price : {3} , Quantity : {4}". format(self.__code , self.__name , self.__firm , self.__price , self.__quantity)
    
class Promotion :
    def __init__(self , value : int , list_of_codes : list , expiration_date : str) :
        self.__value = value
        self.__list_of_codes = list_of_codes
        self.__expiration_date = expiration_date
        
    def get_value(self) :
        return self.__value
    
    def get_list_of_codes(self) :
        return self.__list_of_codes
    
    def get_expiration_date(self) :
        return self.__expiration_date
    
    def __str__(self) :
        return "Value : {0} , List of codes : {1} , Expiration date : {2}". format(self.__value , self.__list_of_codes , self.__expiration_date)
    
    def __repr__(self) :
        return "Value : {0} , List of codes : {1} , Expiration date : {2}". format(self.__value , self.__list_of_codes , self.__expiration_date)