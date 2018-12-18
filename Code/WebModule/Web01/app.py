from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    posts = [
        {
            "title": "La La Land",
            "content": "Land of Dream",
            "author": "Đình Tiến",
            "author_sex": 1
        },
        {
            "title": "Fast And Furious",
            "content": "Vin Diesel",
            "author": "Sao Mai",
            "author_sex": 0
        }
    ]

    return render_template('index.html', posts=posts)

@app.route('/hello')
def say_hello():
    return "Hello from the other side"

@app.route('/say-hi/<name>/<age>')
def say_hi(name, age):
    return "Hi {}, you're {} years old".format(name, age)

@app.route('/sum/<int:x>/<int:y>')
def sum(x, y):
    return "Sum is " + str(x + y)

if __name__ == '__main__':
  app.run(debug=True)
  