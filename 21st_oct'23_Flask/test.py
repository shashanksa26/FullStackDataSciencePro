from flask import Flask, request

app = Flask(__name__)

@app.route("/test")
def test():
    return f" this my test function"

@app.route('/name')
def print_name():
    return f"Shashank"

@app.route('/calci')
def calci():
    add = 10+6
    str_add = str(add)
    return str_add

@app.route('/user')
def user_name():
    data = request.args.get('name')
    return f"{data}"

if __name__ == '__main__':
    app.run(host="0.0.0.0")