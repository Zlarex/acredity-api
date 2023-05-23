from rest_framework import serializers
from ..models.item_akreditasi import ItemAkreditasiMahasiswa

class ItemAkreditasiMahasiswaSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = ItemAkreditasiMahasiswa
    fields = '__all__'
    extra_kwargs = {
      'password': {'write_only': True},
    }