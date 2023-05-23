
from django.db import models
from .mahasiswa import Mahasiswa
from enum import Enum

class BidangAkreditasi(Enum):
  CPBidangSI = 'CPBidangSI'
  CPBidangTI = 'CPBidangTI'
  CPBidangIK = 'CPBidangIK'
  CPBidangSK = 'CPBidangSK'
  CPBidangRPL = 'CPBidangRPL'
  PKM = 'PKM'
  SertifikasiDosen = 'SertifikasiDosen'
  SertifikatMahasiswa = 'SertifikatMahasiswa'

class StatusAkreditasi(Enum):
  PENDING = 'PENDING'
  VALID = 'VALID'
  INVALID = 'INVALID'

class ItemAkreditasiMahasiswa(models.Model):
  nama = models.CharField(max_length=50)
  status = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in StatusAkreditasi], default=StatusAkreditasi.PENDING)
  bidang = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in BidangAkreditasi])
  mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)