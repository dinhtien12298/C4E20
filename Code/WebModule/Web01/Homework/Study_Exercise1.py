from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def about_me():
    info = {
        "name": "Tien Nguyen Dinh",
        "age": 20,
        "university": "Hanoi University Of Science and Technology",
        "hobbies": "Reading and Outing",
        "dog": "Poodle"
    }
    return render_template('about_me.html', info=info)

@app.route('/school')
def school():
    return redirect("https://techkids.vn/")

if __name__ == '__main__':
  app.run(debug=True)
 