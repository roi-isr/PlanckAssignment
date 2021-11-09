"""Spinning up a Flask server that listens to incoming requests on localhost in port 5000"""

from flask import Flask, jsonify, abort
from flask_cors import CORS

from models.menu_data_query import MenuDataQuery
from utility.http_request import send_http_request

app = Flask(__name__)
CORS(app)  # enable connections from all domains


# TODO: update daily
@app.route('/<category>', methods=['GET'])
def get_all_items_by_category(category):
    if category not in ('drinks', 'pizzas', 'desserts'):
        abort(404)

    json_menu_data = send_http_request(
        "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod"
        "=pickup"
    )

    menu_query = MenuDataQuery(json_data=json_menu_data)

    selected_items_for_response = (menu_query.get_all_items_by_category(category=category.title(),
                                                                        fields_to_filter=(
                                                                            'dishName', 'dishId', 'dishDescription',
                                                                            'dishPrice')))
    return jsonify(selected_items_for_response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
