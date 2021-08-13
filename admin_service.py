from entities import Product , Promotion 
from exceptions import DuplicateException , NotFoundException

class AdminService :
    def __init__(self , product_list) :
        self.__product_list = product_list
        self.__promotion_list = []
    
    def get_product_list(self) :
        return self.__product_list
    
    def get_promotion_list(self) :
        return self.__promotion_list
        
    def __position(self , product_code : str) :
        for index in range(len(self.__product_list)) :
            if product_code == self.__product_list[index].get_code():
                return index
        return None
    
    def add_new_product(self , new_product : Product) :
        if new_product in self.__product_list :
            raise DuplicateException(new_product)
        self.__product_list.append(new_product)
        with open("products.txt" , "a+") as g :
            g.write("\n{0} , {1} , {2} , {3} , {4}". format(new_product.get_code() , new_product.get_name() , new_product.get_firm() , new_product.get_price() , new_product.get_quantity()))

    def delete_product(self , identification_code : str) :
        pos = self.__position(identification_code)
        if pos is None :
            raise NotFoundException(identification_code)
        with open("products.txt" , "r") as f :
            content = f.readlines()
        with open("products.txt" , "w") as g :
            for line in content :
                if line.strip("\n").split(" , ")[0] != identification_code :
                   g.write(line)
        del self.__product_list[pos]
        
    def update_product(self , identification_code : str , new_code , new_name , new_firm , new_price , new_quantity) :
        pos = self.__position(identification_code) 
        if pos is None :
            raise NotFoundException(identification_code)
        self.__product_list[pos].set_code(new_code)
        self.__product_list[pos].set_name(new_name)
        self.__product_list[pos].set_firm(new_firm)
        self.__product_list[pos].set_price(new_price)
        self.__product_list[pos].set_quantity(new_quantity)
        with open("products.txt" , "r") as f :
            content = f.readlines()
        with open("products.txt" , "w") as g :
            for line in content :
                if line.strip("\n").split(" , ")[1] != identification_code :
                    g.write(line)
                else :
                    g.write(new_code + " , " + new_name + " , " + new_firm + " , " + str(new_price) + " , " + str(new_quantity) + "\n")
        
    def get_all(self) :
        return self.__product_list
    
    def get_all_from_firm(self , requested_firm) :
        requested_products = []
        for index in range(len(self.__product_list)) :
            if requested_firm == self.__product_list[index].get_firm() :
                requested_products.append(self.__product_list[index])
        return requested_products       
    
    def add_promotion(self , new_promotion : Promotion) :
        for x in new_promotion.get_list_of_codes() :
            pos = self.__position(x)
            if pos is None :
                raise NotFoundException(x)
            for promotion in self.__promotion_list :
               for i in promotion.get_list_of_codes() :
                    if x == i :
                        promotion.get_list_of_codes().remove(i)
                        if(len(promotion.get_list_of_codes()) == 0) :
                            self.__promotion_list.remove(promotion)
        self.__promotion_list.append(new_promotion)            
        
        
        
        
        