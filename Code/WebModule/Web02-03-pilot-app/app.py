from flask import *
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer
from models.user import User
from models.order import Order
from datetime import datetime
from gmail import *

app = Flask(__name__)
app.secret_key = "smdt"

mlab.connect() # tao ra 1 server

# Design pattern (MVC, MVP)

@app.route('/index1')
def index1():
    return render_template('index1.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    all_service = Service.objects()
    return render_template(
        'search.html',
        all_service = all_service
    )

@app.route('/searchsex/<g>')
def searchsex(g):
    all_service = Service.objects(
        gender=g
        # yob__lte=1998,
        # address__exact='Hanoi'
    )
    return render_template(
        'search.html',
        all_service = all_service
    )

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template(
        'customer.html',
        all_customer = all_customer
    )

@app.route('/admin')
def admin():
    if "admin-loggedin" in session:
        if session['admin-loggedin'] == True:
            all_service = Service.objects()
            return render_template(
                'admin.html',
                all_service = all_service
            )
        else:
            return "Đăng nhập chưa mà đòi"
    else:
        return "Đăng nhập chưa mà đòi"

@app.route('/detail/<service_id>')
def detail(service_id):
    if "user-loggedin" in session:
        if session['user-loggedin'] == True:
            detail_service = Service.objects.with_id(service_id)
            if detail_service is not None:
                return render_template('detail.html', detail_service=detail_service)
            else:
                return 'Service is not found'
        else:
            return redirect(url_for('signin'))
    else:
        return redirect(url_for('signin'))

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return 'Service is not found'

@app.route('/new-service', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form

        name = form['name']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        phone = form['phone']
        address = form['address']
        status = form['status']
        description = form['description']
        measurements = form['measurements']

        new_service = Service(
            name=name,
            yob=yob,
            gender=gender,
            height=height,
            phone=phone,
            address=address,
            status=status,
            description=description,
            measurements=measurements
        )
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/update-service/<service_id>', methods=['GET','POST'])
def update(service_id):
    update_service = Service.objects.with_id(service_id)
    if update_service is not None:
        if request.method == 'GET':
            return render_template('update-service.html',update_service=update_service)
        elif request.method == 'POST':
            form = request.form

            name = form['name']
            yob = form['yob']
            height = form['height']
            phone = form['phone']
            address = form['address']
            status = form['status']

            update_service.update(set__name=name)
            update_service.update(set__yob=yob)
            update_service.update(set__phone=phone)
            update_service.update(set__height=height)
            update_service.update(set__address=address)
            update_service.update(set__status=status)
    else:
        return 'Service is not found'
    return redirect(url_for('admin'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login-admin.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']

        if username == 'admin' and password == 'admin':
            session['admin-loggedin'] = True
            return redirect(url_for('admin'))   
        else:
            return 'Sai vcl'

@app.route('/logout')
def logout():
    session['admin-loggedin'] = False
    session['user-loggedin'] = False
    return redirect(url_for('index'))

@app.route('/sign-up', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('sign-up.html')
    elif request.method == 'POST':
        form = request.form

        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']
        
        all_user = User.objects(username=username)
        
        if len(all_user) > 0:
            return 'Username is existed, please use other username'
        else:
            new_user = User(
                fullname=fullname,
                email=email,
                username=username,
                password=password
            )
            new_user.save()
            return redirect(url_for('signin'))
        return "abc"

@app.route('/sign-in', methods=['GET','POST'])
def signin():
    if request.method == 'GET':
        return render_template('login-user.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']

        found_user = User.objects(username=username,password=password)

        if found_user:
            session['user-loggedin'] = True
            user = User.objects.get(username=username)
            session["user_id"] = str(user.id)
            return redirect(url_for('search'))   
        else:
            return 'Sai vcl'

@app.route('/order/<service_id>', methods=['GET','POST'])
def order(service_id):
    if "user-loggedin" in session:
        if session['user-loggedin'] == True:
            new_order = Order(
                user_id=session["user_id"],
                service_id=service_id,
                order_time=datetime.now(),
                is_accepted=False
            )
            new_order.save()
            return 'Đã gửi yêu cầu'
        else:
            return redirect(url_for('signin'))
    else:
        return redirect(url_for('signin'))

@app.route('/ordered')
def ordered():
    if "admin-loggedin" in session:
        if session['admin-loggedin'] == True:
            user_order = User.objects()
            all_order = Order.objects(is_accepted=False)
            return render_template(
                'ordered.html',
                user_order = user_order,
                all_order = all_order
            )
        else:
            return "Đăng nhập chưa mà đòi"
    else:
        return "Đăng nhập chưa mà đòi"

@app.route('/accepted-order/<order_id>/<user_id>')
def accepted_order(order_id, user_id):
    user_order = User.objects.with_id(user_id)
    accepted_order = Order.objects.with_id(order_id)
    if accepted_order is not None and user_order is not None:
        accepted_order.update(set__is_accepted=True)
        gmail = GMail('tiennguyendinh.1998@gmail.com','neverhate')
        msg = Message('PHÊ DUYỆT',to=user_order.email,html="Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của ‘Mùa Đông Không Lạnh’")
        gmail.send(msg)
        return redirect(url_for('ordered'))
    else:
        return 'Order is not found'

if __name__ == '__main__': # kiem tra xem co chay truc tiep hay khong
  app.run(debug=True)