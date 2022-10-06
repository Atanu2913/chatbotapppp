from flask import Flask, json, jsonify, request
import time

app = Flask(__name__)
@app.route("/bot", methods=["POST"])


# response
def response():
    query = dict(request.form)['query']
    result = query + " " + time.ctime()
    return jsonify({"response" : result}) 


if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0",)
    app.run(host="0.0.0.0",)
    