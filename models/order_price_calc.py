import functools

from models.menu_data_query import MenuDataQuery


class OrderPriceCalc:
    """This class is responsible for converting JSON order to a total price"""

    def __init__(self, menu_query: MenuDataQuery, order):
        self.order_dict = json_data = order
        self.menu_query = menu_query

    def calculate_total_price(self):
        return functools.reduce(lambda acc, item: acc + sum(
            [int((self.__get_item_price(category=cat, _id=int(_id.split('_')[1])))
                 for _id in ids)
             for cat, ids in self.order_dict.items()]
        ), self.order_dict)

    def __get_item_price(self, category: str, _id: int):
        total_price = self.menu_query.get_item_by_category_and_id(
            category=category,
            _id=_id
        )['dishPrice']

        return int(total_price)
