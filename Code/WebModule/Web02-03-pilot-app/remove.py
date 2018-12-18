from models.service import Service
import mlab

mlab.connect()

del_service = Service.objects()

del_service.delete()