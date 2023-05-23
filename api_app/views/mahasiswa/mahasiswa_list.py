from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from ...repositories.mahasiswa_repository import MahasiswaRepository

class MahasiswaListAPIView(APIView):
  mahasiswa_repository = MahasiswaRepository()

  def get(self, request):
    mahasiswa = self.mahasiswa_repository.find_all()
    return Response(mahasiswa)

  def post(self, request):
    mahasiswa_id = self.mahasiswa_repository.create(request.data)
    if mahasiswa_id is not None:
      return Response({'id': mahasiswa_id}, status=201)
    return Response(status=400)