from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/foods', methods=['GET'])
def get_json_data():
    #time.sleep(1)
    data = [
               {
                   "name": "Spaghetti",
                   "url": "https://www.bowlofdelicious.com/wp-content/uploads/2023/07/one-pot-spaghetti-with-meat-sauce-square-500x375.jpg",
                   "description": "Spaghetti is a long, thin, solid, cylindrical pasta. It is a staple food of traditional Italian cuisine.",
                   "price": 10
               },
               {
                   "name": "Fettuccine Alfredo",
                   "url": "https://www.modernhoney.com/wp-content/uploads/2018/08/Fettuccine-Alfredo-Recipe-1.jpg",
                   "description": "Fettuccine Alfredo is a pasta dish made from fettuccine pasta tossed with Parmesan cheese and butter.",
                   "price": 12
               },
               {
                   "name": "Penne Arrabiata",
                   "url": "https://www.saltandlavender.com/wp-content/uploads/2019/04/easy-pasta-arrabiata-recipe-1.jpg",
                   "description": "Penne Arrabiata is a spicy Italian pasta dish made with penne pasta, tomatoes, garlic, and red chili peppers.",
                   "price": 9
               }
           ]

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)