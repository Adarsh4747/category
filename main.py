import os
from flask import Flask, request, jsonify
import category


app = Flask(__name__)



# Accepts POST requests at /webhook endpoint
@app.route('/summary', methods=['POST'])
def index():
    summary=request.json['summary']
    r=category.promptmaker(summary)
    return ({"result":r})


if __name__=="__main__":
    app.run(debug=True,port=6000)

#It is category
