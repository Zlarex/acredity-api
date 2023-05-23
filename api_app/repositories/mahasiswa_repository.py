import bcrypt
from ..models.mahasiswa import Mahasiswa
from ..serializers import MahasiswaSerializer

class MahasiswaRepository:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super().__new__(cls, *args, **kwargs)
    return cls._instance

  def get_all_mahasiswa(self):
    mahasiswa = Mahasiswa.objects.all()
    serializer = MahasiswaSerializer(mahasiswa, many=True)
    return serializer.data

  def get_mahasiswa_by_id(self, mahasiswa_id):
    try:
      mahasiswa = Mahasiswa.objects.get(id=mahasiswa_id)
      serializer = MahasiswaSerializer(mahasiswa)
      return serializer.data
    except Mahasiswa.DoesNotExist:
      return None

  def create_mahasiswa(self, data):
    password = data.pop('password')
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    data['password'] = hashed_password.decode()

    serializer = MahasiswaSerializer(data=data)
    if serializer.is_valid():
      mahasiswa = serializer.save()
      return mahasiswa.id
    return None

  def update_mahasiswa(self, mahasiswa_id, data):
    try:
      mahasiswa = Mahasiswa.objects.get(id=mahasiswa_id)
      password = data.pop('password', None)
      if password is not None:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        data['password'] = hashed_password.decode()

      serializer = MahasiswaSerializer(instance=mahasiswa, data=data, partial=True)
      if serializer.is_valid():
        serializer.save()
        return True
      return False
    except Mahasiswa.DoesNotExist:
      return False

  def delete_mahasiswa(self, mahasiswa_id):
    try:
      mahasiswa = Mahasiswa.objects.get(id=mahasiswa_id)
      mahasiswa.delete()
      return True
    except Mahasiswa.DoesNotExist:
      return False
