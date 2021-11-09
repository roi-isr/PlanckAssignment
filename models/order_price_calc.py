import functools
from utility.serializer import serialize_json_to_dict


class OrderPriceCalc:
    """This class is responsible for converting JSON order to a total price"""
    def __init__(self, json_order: str):
        self.order_dict = serialize_json_to_dict(json_data=json_order)

    def calculate_total_price(self):
