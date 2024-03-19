from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/foods', methods=['GET'])
def get_json_data():
    time.sleep(1)
    data = [
                {
                    "id": "be5b0bd7-5fdb-4cfb-8ae4-3755f79e5623",
                    "name": "Pizza",
                    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Pizza-3007395.jpg/1920px-Pizza-3007395.jpg",
                    "description": "Pizza, dish of Italian origin consisting of a flattened disk of bread dough topped with some combination of olive oil, oregano, tomato, olives, mozzarella or other cheese, and many other ingredients, baked.",
                    "price": 10
                },
                {
                    "id": "a1387016-0c74-4300-b08f-3c825313d34b",
                    "name": "Fish and chips",
                    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Fish_and_chips_blackpool.jpg/275px-Fish_and_chips_blackpool.jpg",
                    "description": "Fish and chips is a hot dish consisting of fried fish in batter, served with chips. The dish originated in England, where these two components had been introduced from separate immigrant cultures.",
                    "price": 15
                },
                {
                    "id": "da244261-2166-446b-8dae-b2f087102bf5",
                    "name": "Fried chicken",
                    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Fried_chicken%2C_fried_okra_and_mac_%26_cheese_from_Mary_Mac%27s_Tea_Room_in_Atlanta.jpg/1920px-Fried_chicken%2C_fried_okra_and_mac_%26_cheese_from_Mary_Mac%27s_Tea_Room_in_Atlanta.jpg",
                    "description": "Fried chicken, also known as Southern fried chicken, is a dish consisting of chicken pieces that have been coated with seasoned flour or batter and pan-fried, deep fried, pressure fried, or air fried.",
                    "price": 8
                },
                {
                    "id": "e49b301b-9627-4531-8f04-5305431d9551",
                    "name": "Hamburger",
                    "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/4/47/Hamburger_%28black_bg%29.jpg",
                    "description": "A hamburger, or simply burger, is a food consisting of fillings—usually a patty of ground meat, typically beef—placed inside a sliced bun or bread roll.",
                    "price": 13
                },
           ]
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)