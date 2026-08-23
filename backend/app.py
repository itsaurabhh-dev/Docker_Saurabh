from flask import Flask , request

app = Flask(__name__)

detail = []

@app.route("/submit" , methods = ["POST","GET"])
def submit():
    name = request.form["name"]
    email = request.form["email"]

    detail.append({
        "name" : name,
        "email" : email
    })

    return "successful submited"

@app.route("/api")
def api():
    return detail

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug=True)
