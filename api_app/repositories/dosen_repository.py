import bcrypt
from ..models.dosen import Dosen

class DosenRepository:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super().__new__(cls, *args, **kwargs)
    return cls._instance

  def find_all(self):
    dosen_list = Dosen.objects.all()
    return dosen_list
  
  def find_by_nip(self, nip):
    dosen = Dosen.objects.get(nip=nip)
    return dosen
  
  def create(self, data):
    password = data.pop('password')
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    data['password'] = hashed_password.decode()

    try:
      dosen = Dosen.objects.create(**data)
      return dosen.id
    except Exception as e:
      return None

  def update(self, nip, data):
    try:
      dosen = Dosen.objects.get(nip=nip)
      password = data.pop('password', None)
      if password is not None:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        data['password'] = hashed_password.decode()

      for key, value in data.items():
        setattr(dosen, key, value)
      dosen.save()
      return True
    except Dosen.DoesNotExist:
      return False

  def delete(self, nip):
    try:
      dosen = dosen.objects.get(nip=nip)
      dosen.delete()
      return True
    except Dosen.DoesNotExist:
      return False