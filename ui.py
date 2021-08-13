from admin_service import AdminService
from client_service import ClientService
from entities import Product , Promotion
from validation import ProductValidator , PromotionValidator
from exceptions import ProgramError

class ConsoleUI :
    def __init__(self , admin_service : AdminService , client_service : ClientService) :
        self.__admin_service = admin_service 
        self.__client_service = client_service
        self.__product_validator = ProductValidator()
        self.__promotion_validator = PromotionValidator()
    
    def __print_menu_1(self) :
        print("1.Admin Menu ")
        print("2.Client Menu ")
        print("0.Exit ")
        
    def __print_admin_menu(self) :
        print("1.Add product ")
        print("2.Delete product ")
        print("3.Update product ")
        print("4.View product list ")
        print("5.View product list based on firm ")
        print("6.Add promotion ")
        print("0.Back ")
        
    def __add_product(self) :
        code = input("Product code : ")
        self.__product_validator.code_validator(code)
        name = input("Product name : ")
        firm = input("Product firm : ")
        price = input("Product price : ")
        self.__product_validator.price_validator(price)
        quantity = input("Product quantity : ")
        self.__product_validator.quantity_validator(quantity)
        product = Product(code , name , firm , float(price) , int(quantity))
        self.__admin_service.add_new_product(product)
        print("Product added successfully!")
        
    def __delete_existent_product(self) :
        code = input("Product code to be deleted : ")
        self.__product_validator.code_validator(code)
        self.__admin_service.delete_product(code)
        print("Product deleted successfully!")
   
    def __update_existent_product(self) :
        product_to_be_updated_code = input("Product code : ")
        self.__product_validator.code_validator(product_to_be_updated_code)
        new_code = input("Product new code : ")
        self.__product_validator.code_validator(new_code)
        new_name = input("Product new name : ")
        new_firm = input("Product new firm : ")
        new_price = input("Product new price : ")
        self.__product_validator.price_validator(new_price)
        new_quantity = input("Product new quantity : ")
        self.__product_validator.quantity_validator(new_quantity)
        self.__admin_service.update_product(product_to_be_updated_code , new_code , new_name , new_firm , new_price , new_quantity)
        print("Product updated successfully!")
   
    def __view_product_list(self) :
        print(*self.__admin_service.get_all() , sep = "\n\n")
        
    def __view_firm_product_list(self) :
        firm_name = input("Firm name : ")
        print(*self.__admin_service.get_all_from_firm(firm_name) , sep = "\n\n")
        
    def __new_promotion(self) :
        value = input("Promotion value : ")
        self.__promotion_validator.value_validator(value)
        codes = input("Products to apply promotion to : ")
        list_of_codes = codes.split()
        for code in list_of_codes :
            self.__product_validator.code_validator(code)
        expiration_date = input("Expiration date : ")
        self.__promotion_validator.expiration_date_validator(expiration_date)
        promotion = Promotion(int(value) , list_of_codes , expiration_date)
        self.__admin_service.add_promotion(promotion)
        print("Promotion added successfully")
        
    def __print_client_menu(self) :
        print("1.Buy product ") 
        print("2.View product list ")
        print("3.View products in budget ")
        print("4.View products in promotion ")
        print("0.Back ")
    
    def __buy(self) :
        product_code = input("Product code : ")
        self.__product_validator.code_validator(product_code)
        product_quantity = input("Product quantity : ")
        self.__product_validator.quantity_validator(product_quantity)
        self.__client_service.buy_product(product_code , int(product_quantity))
        print("Product bought successfully")
    
    def __view_products_in_budget(self) :
        price = input("Budget : ")
        self.__product_validator.price_validator(price)
        self.__client_service.products_in_budget(float(price))
    
    def __view_products_in_promotion(self) :
        self.__client_service.products_in_promotion()
    
    def run(self) :
        while True :
            self.__print_menu_1()
            try :
                command_1 = int(input("Choose the command : ").strip())
                if command_1 == 0 :
                    break
                elif command_1 == 1 :
                    while True :
                        self.__print_admin_menu()
                        command_2 = int(input("Choose the command : ").strip())
                        if command_2 == 0 :
                            break
                        elif command_2 == 1 :
                            self.__add_product()
                        elif command_2 == 2 :
                            self.__delete_existent_product()
                        elif command_2 == 3 :
                            self.__update_existent_product()
                        elif command_2 == 4 :
                            self.__view_product_list()
                        elif command_2 == 5 :
                            self.__view_firm_product_list()
                        elif command_2 == 6 :
                            self.__new_promotion()
                elif command_1 == 2 :
                    while True :
                        self.__print_client_menu()
                        command_3 = int(input("Choose the command : ").strip())
                        if command_3 == 0 :
                            break
                        elif command_3 == 1 :
                            self.__buy()
                        elif command_3 == 2 :
                            self.__view_product_list()
                        elif command_3 == 3 :
                            self.__view_products_in_budget()
                        elif command_3 == 4 :
                            self.__view_products_in_promotion()
            except ProgramError as error :
                print(error)
            