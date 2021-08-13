from admin_service import AdminService
from client_service import ClientService
from ui import ConsoleUI 
from file_repository import FileRepository

products = FileRepository()
products.read_product_details()

admin = AdminService(products.get_product_list())
client = ClientService(admin.get_product_list() , admin.get_promotion_list())

ui = ConsoleUI(admin , client)

ui.run()