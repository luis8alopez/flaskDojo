from flask import Flask 
from flask import jsonify
from flask import request
import json
import array

Myapp = Flask(__name__)

arr = ['Not defined','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII','XXIII','XXIV','XXV','XXVI','XXVII','XXVIII','XXIX','XXX','XXXI','XXXII','XXXIII','XXXIV','XXXV','XXXVI','XXXVII','XXXVIII','XXXIX','XL','XLI','XLII','XLIII','XLIV','XLV','XLVI','XLVII','XLVIII','XLIX','L','LI','LII','LIII','LIV','LV','LVI','LVII','LVIII','LIX','LX','LXI','LXII','LXIII','LXIV','LXV','LXVI','LXVII','LXVIII','LXIX','LXX','LXXI','LXXII','LXXIII','LXXIV','LXXV','LXXVI','LXXVII','LXXVIII','LXXIX','LXXX','LXXXI','LXXXII','LXXXIII','LXXXIV','LXXXV','LXXXVI','LXXXVII','LXXXVIII','LXXXIX','XC','XCI','XCII','XCIII','XCIV','XCV','XCVI','XCVII','XCVIII','XCIX','C']

b = arr

@Myapp.route('/')
def fromArabicToRoman():

    n = request.args.get('number')
    number = int(n)

    if(number <0 or number >100):
        return jsonify({'message': 'The number must be between 1 and 100, both included'})

    response = Myapp.response_class(
        response=json.dumps({"in arabic ": number,"in roman ":b[number]}),
        status=200,
        mimetype='application/json'
    )
    return response

@Myapp.route('/numbers',methods=['GET','POST'])
def convertNumber():
    return b