from flask import Flask,request,render_template
app = Flask('__name__')

@app.route('/calculator')
def cal_page():
    return render_template('css_calci.html')

@app.route("/math",methods=["POST"])
def calculator():
    ops = request.form['operation'] # operation is id in forms file css_calci.html
    first_num = int(request.form['num1'])
    second_num = int(request.form['num2'])

    if(ops == 'add'):
        r = first_num + second_num
        return f"Addition of {first_num} and {second_num} = {r}"

    if(ops == 'subtract'):
        r = first_num - second_num
        return f"Subtraction of {first_num} and {second_num} = {r}"
    
    if(ops == 'multiply'):
        r = first_num * second_num
        return f"Multiplication of {first_num} and {second_num} = {r}"
    
    if(ops == 'divide'):
        r = first_num / second_num
        return f"Division of {first_num} and {second_num} = {r}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')