from django.urls import path
from .views.mahasiswa_api_view import MahasiswaListAPIView, MahasiswaDetailAPIView
from .views.kaprodi_api_view import KaprodiListAPIView, KaprodiDetailAPIView

urlpatterns = [
  path('mahasiswa', MahasiswaListAPIView.as_view(), name='mahasiswa-list'),
  path('mahasiswa/<int:nim>', MahasiswaDetailAPIView.as_view(), name='mahasiswa-detail'),
  path('kaprodi', KaprodiListAPIView.as_view(), name='kaprodi-list'),
  path('kaprodi/<int:nip>', KaprodiDetailAPIView.as_view(), name='kaprodi-detail'),
]
