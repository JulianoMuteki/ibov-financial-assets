from flask import Flask, request, jsonify

from yahooLib import get_Info
from yahooLib import get_History


app = Flask(__name__)

@app.route('/history', methods=['GET'])
def get_history():
    dateFilter = request.args.get('dateFilter')
    ticker = request.args.get('ticker')

    # Call the method and store the return value in a variable
    result = get_History(ticker, dateFilter)
    
    return result

@app.route('/info', methods=['GET'])
def info():
    ticker = request.args.get('ticker')

    # Call the method and store the return value in a variable
    result = get_Info(ticker)
    
    return result

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
