from rest_framework import serializers
from ..models.kaprodi import Kaprodi

class KaprodiSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Kaprodi
    fields = '__all__'
    extra_kwargs = {
      'password': {'write_only': True},
    }