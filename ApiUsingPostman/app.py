from flask import render_template, Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # To render Homepage
def home_page():
    return render_template('index.html')


@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if request.method == 'POST':
        try:
            operation = request.form['operation']
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
        except ValueError:
            return render_template('results.html', result='Error! Please, enter numbers only!')
        if operation == 'add':
            r = num1 + num2
            result = f'{str(num1)} + {str(num2)} = {str(r)}'
        elif operation == 'subtract':
            r = num1 - num2
            result = f'{str(num1)} - {str(num2)} = {str(r)}'
        elif operation == 'multiply':
            r = num1 * num2
            result = f'{str(num1)} * {str(num2)} = {str(r)}'
        elif operation == 'divide':
            try:
                r = num1 / num2
                result = f'{str(num1)} / {str(num2)} = {str(r)}'
            except ZeroDivisionError:
                result = "Error! Division by 0 is not allowed."
        else:
            result = "Error! Given operation is not supported."
        return render_template('results.html', result=result)


@app.route('/postman-test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return jsonify({"response": "Get Request Called. App is running (200)"})
    elif request.method == 'POST':
        req_json = request.json
        operation = req_json['operation']
        num1 = req_json['num1']
        num2 = req_json['num2']
        if operation == 'add':
            r = num1 + num2
            result = f'{str(num1)} + {str(num2)} = {str(r)}'
        elif operation == 'subtract':
            r = num1 - num2
            result = f'{str(num1)} - {str(num2)} = {str(r)}'
        elif operation == 'multiply':
            r = num1 * num2
            result = f'{str(num1)} * {str(num2)} = {str(r)}'
        elif operation == 'divide':
            try:
                r = num1 / num2
                result = f'{str(num1)} / {str(num2)} = {str(r)}'
            except ZeroDivisionError:
                result = "Error! Division by 0 is not allowed."
        else:
            result = "Error! Given operation is not supported."
        return result


if __name__ == '__main__':
    app.run(debug=True, port=8000)
