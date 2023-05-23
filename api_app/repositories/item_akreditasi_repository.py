import bcrypt
from ..models.item_akreditasi import ItemAkreditasiMahasiswa
from ..serializers.item_akreditasi_serializer import ItemAkreditasiMahasiswaSerializer

class ItemAkreditasiMahasiswaRepository:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super().__new__(cls, *args, **kwargs)
    return cls._instance

  def find_all(self):
    return ItemAkreditasiMahasiswa.objects.all()