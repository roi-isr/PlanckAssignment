from utility.serializer import serialize_json_to_dict


class MenuDataQuery:
    """A class for abstracting and querying the incoming JSON data from 10bis API.
    Builds a table data structure in memory for simpler data representation"""

    def __init__(self, json_data):
        menu_dict = serialize_json_to_dict(json_data).get("Data", {})  # Convert JSON data to python dictionary
        if not menu_dict:
            raise ValueError("Not Data field in the income request's JSON")

        self.category_list = menu_dict.get("categoriesList", [])
        if not self.category_list:
            raise ValueError("Not categoriesList field in the income request's JSON")

    def get_all_items_by_category(self, category: str):

        requested_category_list = list(
            filter(lambda cat: cat["categoryName"] == category, self.category_list)
        )

        requested_dish_list = [category_item["distList"] for category_item in requested_category_list]

        print(requested_dish_list)
