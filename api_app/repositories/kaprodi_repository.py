import bcrypt
from ..models.kaprodi import Kaprodi
from ..serializers.kaprodi_serializer import KaprodiSerializer

class KaprodiRepository:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super().__new__(cls, *args, **kwargs)
    return cls._instance

  def find_all(self):
    kaprodi = Kaprodi.objects.all()
    serializer = KaprodiSerializer(kaprodi, many=True)
    return serializer.data
  
  def find_by_nip(self, nip):
    try:
      kaprodi = Kaprodi.objects.get(nip=nip)
      serializer = KaprodiSerializer(kaprodi)
      return serializer.data
    except Kaprodi.DoesNotExist:
      return None
  
  def create(self, data):
    password = data.pop('password')
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    data['password'] = hashed_password.decode()

    serializer = KaprodiSerializer(data=data)
    if serializer.is_valid():
      kaprodi = serializer.save()
      return kaprodi.id
    return None
  
  def update(self, nip, data):
    try:
      kaprodi = kaprodi.objects.get(nip=nip)
      password = data.pop('password', None)
      if password is not None:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        data['password'] = hashed_password.decode()

      serializer = KaprodiSerializer(instance=kaprodi, data=data, partial=True)
      if serializer.is_valid():
        serializer.save()
        return True
      return False
    except Kaprodi.DoesNotExist:
      return False

  def delete(self, nip):
    try:
      kaprodi = kaprodi.objects.get(nip=nip)
      kaprodi.delete()
      return True
    except Kaprodi.DoesNotExist:
      return False