import bcrypt
from ..models.mahasiswa import Mahasiswa
from ..serializers.mahasiswa_serializer import MahasiswaSerializer

class MahasiswaRepository:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super().__new__(cls, *args, **kwargs)
    return cls._instance

  def find_all(self):
    return Mahasiswa.objects.all()
  
  def find_by_nim(self, nim):
    return Mahasiswa.objects.get(nim=nim)

  def create(self, data):
    password = data.pop('password')
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    data['password'] = hashed_password.decode()

    try:
        mahasiswa = Mahasiswa.objects.create(**data)
        return mahasiswa.id
    except Exception as e:
        return None


  def update(self, nim, data):
    try:
      mahasiswa = Mahasiswa.objects.get(nim=nim)
      password = data.pop('password', None)
      if password is not None:
          hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
          data['password'] = hashed_password.decode()

      for key, value in data.items():
          setattr(mahasiswa, key, value)
      
      mahasiswa.save()
      return True
    except Mahasiswa.DoesNotExist:
      return False

  def delete(self, nim):
    try:
      mahasiswa = Mahasiswa.objects.get(nim=nim)
      mahasiswa.delete()
      return True
    except Mahasiswa.DoesNotExist:
      return False
