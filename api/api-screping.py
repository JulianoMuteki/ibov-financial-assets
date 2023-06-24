from flask import Flask, request, jsonify

from web import my_method

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    string_param = request.args.get('string_param')

    # Call the method and store the return value in a variable
    result = my_method(string_param)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
