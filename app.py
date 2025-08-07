from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Welcome to Fun Info App</h2>
        <form method="post" action="/result">
            <label>Enter your name:</label>
            <input type="text" name="username">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/result', methods=['POST'])
def result():
    name = request.form['username']
    # You can add your logic here to fetch fun info
    return f"<h3>Hello, {name}! This is your fun info result.</h3>"

if __name__ == '_main_':
    app.run(debug=True)
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Welcome to Fun Info App</h2>
        <form method="post" action="/result">
            <label>Enter your name:</label>
            <input type="text" name="username">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/result', methods=['POST'])
def result():
    name = request.form['username']
    return f"<h3>Hello, {name}! This is your fun info result.</h3>"

if __name__ == '__main__':
    app.run(debug=True)