from django.urls import path
from .views import MahasiswaListAPIView, MahasiswaDetailAPIView

urlpatterns = [
  path('mahasiswa', MahasiswaListAPIView.as_view(), name='mahasiswa-list'),
  path('mahasiswa/<int:mahasiswa_id>', MahasiswaDetailAPIView.as_view(), name='mahasiswa-detail'),
]
