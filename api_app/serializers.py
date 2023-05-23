from rest_framework import serializers
from .models.mahasiswa import Mahasiswa, KelasMahasiswa

class MahasiswaSerializer(serializers.ModelSerializer):
  class KelasMahasiswaField(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return KelasMahasiswa(data)

  kelas = KelasMahasiswaField()
  password = serializers.CharField(write_only=True)

  class Meta:
    model = Mahasiswa
    fields = '__all__'
    extra_kwargs = {
      'password': {'write_only': True},
    }