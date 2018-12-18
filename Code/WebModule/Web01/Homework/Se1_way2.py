from flask import Flask, render_template
app = Flask(__name__)

info = {}
@app.route('/bmi2/<int:weight>/<int:height>')
def bmi2(weight, height):
    bmi = weight / ((height/100)**2)
    info['bmi'] = bmi
    return render_template('bmi.html', info = info)

if __name__ == '__main__':
  app.run(debug=True)
 