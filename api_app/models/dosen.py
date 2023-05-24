from django.db import models
from enum import Enum
import bcrypt

class BidangStudi(Enum):
  SI = 'SI'
  TI = 'TI'
  IK = 'IK'
  SK = 'SK'
  RPL = 'RPL'

  def __str__(self):
    return self.value

# Create your models here.
class Dosen(models.Model):
  nip = models.CharField(max_length=20)
  password = models.CharField(max_length=255)
  nama = models.CharField(max_length=100)
  bidang_studi = models.CharField(max_length=3, choices=[(tag, tag.value) for tag in BidangStudi])

  def set_password(self, raw_password):
    hashed_password = bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt())
    self.password = hashed_password.decode()

  def check_password(self, raw_password):
    return bcrypt.checkpw(raw_password.encode(), self.password.encode())