import bcrypt
from ..models.kaprodi import Kaprodi

class KaprodiRepository:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super().__new__(cls, *args, **kwargs)
    return cls._instance

  def find_all(self):
    kaprodi_list = Kaprodi.objects.all()
    return kaprodi_list
  
  def find_by_nip(self, nip):
    kaprodi = Kaprodi.objects.get(nip=nip)
    return kaprodi
  
  def create(self, data):
    password = data.pop('password')
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    data['password'] = hashed_password.decode()

    kaprodi = Kaprodi(**data)
    kaprodi.save()
    return kaprodi.id

  def update(self, nip, data):
    try:
      kaprodi = Kaprodi.objects.get(nip=nip)
      password = data.pop('password', None)
      if password is not None:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        data['password'] = hashed_password.decode()

      for key, value in data.items():
        setattr(kaprodi, key, value)
      kaprodi.save()
      return True
    except Kaprodi.DoesNotExist:
      return False

  def delete(self, nip):
    try:
      kaprodi = kaprodi.objects.get(nip=nip)
      kaprodi.delete()
      return True
    except Kaprodi.DoesNotExist:
      return False