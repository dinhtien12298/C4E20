from flask import Flask
app = Flask(__name__)


@app.route('/bmi1/<int:weight>/<int:height>')
def bmi1(weight, height):
    bmi = weight / ((height/100)**2)
    if bmi < 16:
        return "You are Severely underweight"
    elif bmi < 18.5:
        return "You are Underweight"
    elif bmi < 25:
        return "You are Normal"
    elif bmi < 30:
        return "You are Overweight"
    else:
        return "You are Obese"

if __name__ == '__main__':
  app.run(debug=True)
 