from flask import Flask, request, jsonify

from yahooLib import get_Info
from yahooLib import get_History


app = Flask(__name__)

@app.route('/history', methods=['GET'])
def get_history():
    string_param = request.args.get('string_param')

    # Call the method and store the return value in a variable
    result = get_History(string_param)
    
    return result

@app.route('/info', methods=['GET'])
def info():
    
    # Call the method and store the return value in a variable
    result = get_Info()
    
    return result

if __name__ == '__main__':
    app.run(debug=True)
