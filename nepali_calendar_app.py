from flask import Flask, request, jsonify
from nepali_calendar import NepaliDateConverter

app = Flask(__name__)
converter = NepaliDateConverter()

@app.route('/')
def index():
    return 'Welcome to Nepali Calendar Web Tool'

@app.route('/convert_bs_to_ad', methods=['POST'])
def convert_bs_to_ad():
    data = request.get_json()
    bs_year = data['bs_year']
    bs_month = data['bs_month']
    bs_day = data['bs_day']
    
    ad_date = converter.bs_to_ad(bs_year, bs_month, bs_day)
    return jsonify({'ad_date': ad_date})

if __name__ == '__main__':
    app.run(debug=True)
