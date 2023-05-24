from rest_framework import serializers
from ..models.dosen import Dosen, BidangStudi

class DosenSerializer(serializers.ModelSerializer):
  class BidangStudiField(serializers.Field):
    def to_representation(self, value):
      return value

    def to_internal_value(self, data):
      return BidangStudi(data)
    
  bidang_studi = BidangStudiField()
  password = serializers.CharField(write_only=True)
  
  class Meta:
    model = Dosen
    fields = '__all__'
    extra_kwargs = {
      'password': {'write_only': True},
    }