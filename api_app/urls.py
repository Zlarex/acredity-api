from django.urls import path
from .views.mahasiswa_api_view import MahasiswaListAPIView, MahasiswaDetailAPIView, MahasiswaLoginAPIView, MahasiswaAkreditasiAPIView
from .views.kaprodi_api_view import KaprodiListAPIView, KaprodiDetailAPIView, KaprodiLoginAPIView
from .views.dosen_api_view import DosenListAPIView, DosenDetailAPIView, DosenLoginAPIView

urlpatterns = [
  path('mahasiswa', MahasiswaListAPIView.as_view(), name='mahasiswa-list'),
  path('mahasiswa/login', MahasiswaLoginAPIView.as_view(), name='mahasiswa-login'),
  path('mahasiswa/<int:nim>', MahasiswaDetailAPIView.as_view(), name='mahasiswa-detail'),
  path('mahasiswa/<int:nim>/akreditasi', MahasiswaAkreditasiAPIView.as_view(), name='mahasiswa-akreditasi'),
  path('kaprodi', KaprodiListAPIView.as_view(), name='kaprodi-list'),
  path('kaprodi/login', KaprodiLoginAPIView.as_view(), name='kaprodi-login'),
  path('kaprodi/<int:nip>', KaprodiDetailAPIView.as_view(), name='kaprodi-detail'),
  path('dosen', DosenListAPIView.as_view(), name='dosen-list'),
  path('dosen/login', DosenLoginAPIView.as_view(), name='dosen-login'),
  path('dosen/<int:nip>', DosenDetailAPIView.as_view(), name='dosen-detail'),
]
