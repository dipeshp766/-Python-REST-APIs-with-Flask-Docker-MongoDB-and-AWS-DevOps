from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/add_two_nums', methods = ["POST"])
def add_two_nums():
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]

    z = x + y

    retJSON = {
        "z": z
    }

    return retJSON, 200
@app.route('/retJSON')
def retJSON():
    ret_json = {
        'Name':'Dipesh',
        'Age': 24,
        'Phones': [
            {
                "phoneName": "Samsung Galaxy S10+",
                "phoneNumber": 5199849280
            },
            {
                "phoneName": "Sony Xperia Z1",
                "phoneNumber": 9726468848
            }
        ]
    }

    return jsonify(ret_json)

if __name__ == "__main__":
    app.run()