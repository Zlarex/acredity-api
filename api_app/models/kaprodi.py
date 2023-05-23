from django.db import models
import bcrypt

class Kaprodi(models.Model):
  nip = models.CharField(max_length=20)
  password = models.CharField(max_length=255)
  nama = models.CharField(max_length=100)

  def set_password(self, raw_password):
    hashed_password = bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt())
    self.password = hashed_password.decode()

  def check_password(self, raw_password):
    return bcrypt.checkpw(raw_password.encode(), self.password.encode())