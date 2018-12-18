from flask import Flask, render_template
app = Flask(__name__)

info = {
        "DinhTien":{
        "name": "Tien Nguyen Dinh",
        "age": 20,
        "university": "Hanoi University Of Science and Technology",
        "hobbies": "Reading and Outing",
        "dog": "Poodle"
        },
        "SaoMai":{
        "name": "Mai Le Sao",
        "age": 21,
        "university": "Culture University",
        "hobbies": "Chatting and Hang Out",
        "dog": "Poodle"        
        }
}
@app.route('/user/<username>')
def user(username):
    if username in info.keys():
        return render_template('user.html', info = info[username])
    else:
        return 'User not found'

if __name__ == '__main__':
  app.run(debug=True)
 