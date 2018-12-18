from models.service import Service
import mlab
from faker import Faker
from random import *

mlab.connect()

fake = Faker()

for i in range(40):
    print('Saving Service', i+1, '......')
    sex = randint(0, 1)

    if sex == 1:
        new_service = Service(
            name = fake.name(),
            yob = randint(1990, 2005),
            gender = sex,
            height = randint(150, 190),
            phone = fake.phone_number(),
            address = fake.address(),
            status = choice(['Bận', 'Rảnh']),
            image = 'static/image/' + choice(['male.jpg','male-profile.jpg']),
            description = sample(['biết nấu ăn', 'thích chụp ảnh', 'chơi guitar', 'thích đọc sách', 'thích du lịch', 'yêu động vật'], 4),
            measurements = [randint(60,100),randint(60,100),randint(60,100)]
        )
    elif sex == 0:
        new_service = Service(
            name = fake.name(),
            yob = randint(1990, 2005),
            gender = sex,
            height = randint(150, 190),
            phone = fake.phone_number(),
            address = fake.address(),
            status = choice(['Bận', 'Rảnh']),
            image = 'static/image/' + choice(['female.jpg','female-profile.jpg']),
            description = sample(['biết nấu ăn', 'thích vẽ', 'chơi piano', 'thích kpop', 'thích du lịch', 'ghét động vật'], 4),
            measurements = [randint(60,100),randint(60,100),randint(60,100)]
        )        

    new_service.save()
