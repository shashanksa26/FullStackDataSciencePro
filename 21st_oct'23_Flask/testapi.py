from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route("/")
# it is  a get request
def show_form():
    return render_template("css_form.html")

@app.route("/submit_data", methods = ['POST'])
def check_password():
    name = request.form.get('username')
    password = request.form.get('password')
    print({name},{password})
    return "User name and Password Received Succesfully ✅"


if __name__ == "__main__":
    app.run(host = "0.0.0.0",port=8000)