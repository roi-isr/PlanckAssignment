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

    def get_all_items_by_category(self, category: str, fields_to_filter=()):
        requested_dish_collection = self.__get_dish_collection_by_category(category=category)

        return self.__extract_fields_from_collection(collection=requested_dish_collection,
                                                     fields_to_filter=fields_to_filter)

    def get_item_by_category_and_id(self, category: str, _id: int, fields_to_filter=()):
        requested_dish_collection = self.__get_dish_collection_by_category(category=category)

        dish_item = self.__filter_dish_collection_by_id(requested_dish_collection, _id=_id)

        if not dish_item:
            return None
        return self.__extract_fields_from_collection(collection=dish_item, fields_to_filter=fields_to_filter)

    def __get_dish_collection_by_category(self, category):
        requested_category_list = list(
            filter(lambda cat: cat["categoryName"] == category, self.category_list)
        )

        # in order to deal with category duplications
        requested_dish_collection = []
        for category_item in requested_category_list:
            requested_dish_collection += category_item["dishList"]
        return requested_dish_collection

    @staticmethod
    def __filter_dish_collection_by_id(requested_dish_collection, _id: int):
        dish_item = list(
            filter(lambda cat: cat["dishId"] == _id, requested_dish_collection)
        )

        return dish_item

    @staticmethod
    def __extract_fields_from_collection(collection, fields_to_filter):
        if fields_to_filter:
            return [{k: doc[k] for k in fields_to_filter} for doc in collection]
        return collection  # in case there are no fields to filter, returns the whole collection as it is
