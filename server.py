from utility.http_request import send_http_request
from models.menu_data_processor import MenuDataProcessor

json_data = send_http_request("https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup")
MenuDataProcessor(json_data=json_data)

