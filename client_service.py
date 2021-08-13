from entities import Product , Promotion
from exceptions import NotFoundException
from datetime import datetime

class ClientService :
    def __init__(self , product_list : list , promotion_list : list) :
        self.__product_list = product_list
        self.__promotion_list = promotion_list
    
    def __position(self , product_code : str) :
        for index in range(len(self.__product_list)) :
            if product_code == self.__product_list[index].get_code():
                return index
        return None
    
    def buy_product(self , identification_code : str , requested_quantity : int) :
        pos = self.__position(identification_code)
        if pos is None :
            raise NotFoundException(identification_code)
        else :
            if self.__product_list[pos].get_quantity() < requested_quantity :
                print("Please select a lower quantity")
            elif self.__product_list[pos].get_quantity() == requested_quantity :
                with open("products.txt" , "r") as f :
                     content = f.readlines()
                with open("products.txt" , "w") as g :
                    for line in content :
                        if line.strip("\n").split(" , ")[1] != identification_code :
                            g.write(line)
                del self.__product_list[pos]
                print("Product bought successfully")
            else :
                print("Product bought successfully")
                self.__product_list[pos].set_quantity(self.__product_list[pos].get_quantity() - requested_quantity)
                with open("products.txt" , "r") as f :
                    content = f.readlines()
                with open("products.txt" , "w") as g :
                    for line in content :
                        if line.strip("\n").split(" , ")[1] != identification_code :
                            g.write(line)
                        else :
                            g.write(str(self.__product_list[pos].get_code()) + " , " + str(self.__product_list[pos].get_name()) + " , " + str(self.__product_list[pos].get_firm()) + " , " + str(self.__product_list[pos].get_price()) + " , " + str(self.__product_list[pos].get_quantity()))
                            g.write("\n")
                        
    def get_all(self) :
        return self.__product_list

    def products_in_budget(self , given_price) :
        ans = []
        for product in self.__product_list :
            if product.get_price() <= given_price :
                ans.append(product)
        ans = sorted(ans , key = lambda x : x.get_price() , reverse = True) 
        print(*ans , sep = "\n\n")
    def products_in_promotion(self) :
        self.__promotion_list = sorted(self.__promotion_list , key = lambda x : x.get_value(), reverse = True)
        prices_after_promotion = {}
        ok = 0
        print("Sorted after promotion value : ")
        for promotion in self.__promotion_list :
            date_object = datetime.strptime(promotion.get_expiration_date() , "%d-%m-%Y")
            if datetime.now() <= date_object :
                print("Promotion value : " + str(promotion.get_value()))
                print("Products in promotion : ")
                products = promotion.get_list_of_codes()
                for product in products :
                    pos = self.__position(product)
                    print(self.__product_list[pos] , "New price : " + str((100 - promotion.get_value()) * self.__product_list[pos].get_price() / 100) , end = "")
                    print()
                    prices_after_promotion[pos] = (100 - promotion.get_value()) * self.__product_list[pos].get_price() / 100
                print()
                print()
                ok = 1
        if ok == 0 :
            print("No active promotion")
        else :
            prices_after_promotion = sorted(prices_after_promotion.items() , key = lambda x : x[1] , reverse = True)
            print("Sorted after new price : ")
            for key in prices_after_promotion :
                print(self.__product_list[key[0]] , "New price : " + str(key[1]) , end = " ")
                print()
                