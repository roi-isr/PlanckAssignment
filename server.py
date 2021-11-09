"""Spinning up a Flask server that listens to incoming requests on localhost in port 5000"""

from flask import Flask, jsonify, abort, request
from flask_cors import CORS

from models.menu_data_query import MenuDataQuery
from models.order_price_calc import OrderPriceCalc
from utility.http_request import send_http_request

app = Flask(__name__)
CORS(app)  # enable connections from all domains


def get_http_data():
    json_menu_data = send_http_request(
        "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod"
        "=pickup"
    )
    return json_menu_data


# TODO: update daily - save in a json file and update once a day


@app.route('/<category>/<_id>', methods=['GET'])
def get_specific_item_by_category(category, _id):
    if category not in ('drinks', 'pizzas', 'desserts'):
        abort(404)

    json_menu_data = get_http_data()

    menu_query = MenuDataQuery(json_data=json_menu_data)

    response_item = menu_query.get_item_by_category_and_id(category=category.title(),
                                                           _id=int(_id),
                                                           fields_to_filter=(
                                                               'dishName', 'dishId', 'dishDescription',
                                                               'dishPrice'))

    if not response_item:
        abort(404)
    else:
        return jsonify(response_item), 200


@app.route('/<category>', methods=['GET'])
def get_all_items_by_category(category):
    if category not in ('drinks', 'pizzas', 'desserts'):
        abort(404)

    json_menu_data = get_http_data()

    menu_query = MenuDataQuery(json_data=json_menu_data)

    response_items = menu_query.get_all_items_by_category(category=category.title(),
                                                          fields_to_filter=(
                                                              'dishName', 'dishId', 'dishDescription',
                                                              'dishPrice'))

    return jsonify(response_items), 200


@app.route('/order', methods=['POST'])
def get_total_price_for_order():
    body_data = request.get_json(force=True)
    # body_data = serialize_json_to_dict(body_json)

    # validate body
    for category in body_data.keys():
        if category not in ('drinks', 'pizzas', 'desserts'):
            return jsonify({"msg": "Invalid body"}), 400

    json_menu_data = get_http_data()

    menu_query = MenuDataQuery(json_data=json_menu_data)

    order_calc = OrderPriceCalc(menu_query=menu_query, order=body_data)

    total_price = order_calc.calculate_total_price()

    return jsonify({"price": total_price}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
