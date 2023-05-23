from django.db import models
from enum import Enum
import bcrypt

class KelasMahasiswa(Enum):
    A = 'A'
    B = 'B'

    def __str__(self):
        return self.value

# Create your models here.
class Mahasiswa(models.Model):
    nim = models.CharField(max_length=9)
    password = models.CharField(max_length=255)
    nama = models.CharField(max_length=100)
    kelas = models.CharField(max_length=1, choices=[(tag, tag.value) for tag in KelasMahasiswa])
    tahun_masuk = models.PositiveIntegerField()
    tahun_keluar = models.PositiveIntegerField()

    def set_password(self, raw_password):
      hashed_password = bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt())
      self.password = hashed_password.decode()

    def check_password(self, raw_password):
      return bcrypt.checkpw(raw_password.encode(), self.password.encode())