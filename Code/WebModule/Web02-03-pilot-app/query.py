from models.service import Service
import mlab

mlab.connect()

all_service = Service.objects()

# id_to_find = '5b7ce40fa6d4c104a8b2b6da'

# hera = Service.objects(id=id_to_find) # => [Service obj]
# hera = Service.objects.get(id=id_to_find) # => Service obj
# service = Service.objects.with_id(id_to_find) # => Service obj (nen dung)

if service is not None:
    print('Before: ')
    print(service.to_mongo())
    service.update(set__yob=2000, set__name='SM')
    service.reload()
    print('After: ')
    print(service.to_mongo())
else:
    print('Not found')