from django.urls import path
from .views.mahasiswa.mahasiswa_list import MahasiswaListAPIView
from .views.mahasiswa.mahasiswa_detail import MahasiswaDetailAPIView
from .views.kaprodi.kaprodi_list import KaprodiListAPIView
from .views.kaprodi.kaprodi_detail import KaprodiDetailAPIView

urlpatterns = [
  path('mahasiswa', MahasiswaListAPIView.as_view(), name='mahasiswa-list'),
  path('mahasiswa/<int:mahasiswa_id>', MahasiswaDetailAPIView.as_view(), name='mahasiswa-detail'),
  
  path('kaprodi', KaprodiListAPIView.as_view(), name='kaprodi-list'),
  path('kaprodi/<int:kaprodi_id>', KaprodiDetailAPIView.as_view(), name='kaprodi-detail'),
]
