from utility.http_request import send_http_request
from models.menu_data_query import MenuDataQuery

json_data = send_http_request("https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup")
a = MenuDataQuery(json_data=json_data)

print(a.get_all_items_by_category(category="Drinks"))

