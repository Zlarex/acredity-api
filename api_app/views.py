from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .repositories.mahasiswa_repository import MahasiswaRepository

class MahasiswaListAPIView(APIView):
  mahasiswa_repository = MahasiswaRepository()

  def get(self, request):
    mahasiswa = self.mahasiswa_repository.get_all_mahasiswa()
    return Response(mahasiswa)

  def post(self, request):
    mahasiswa_id = self.mahasiswa_repository.create_mahasiswa(request.data)
    if mahasiswa_id is not None:
      return Response({'id': mahasiswa_id}, status=201)
    return Response(status=400)

class MahasiswaDetailAPIView(APIView):
  mahasiswa_repository = MahasiswaRepository()

  def get(self, request, mahasiswa_id):
    mahasiswa = self.mahasiswa_repository.get_mahasiswa_by_id(mahasiswa_id)
    if mahasiswa is not None:
      return Response(mahasiswa)
    return Response(status=404)

  def put(self, request, mahasiswa_id):
    success = self.mahasiswa_repository.update_mahasiswa(mahasiswa_id, request.data)
    if success is not None:
      return Response(status=200)
    return Response(status=400)

  def delete(self, request, mahasiswa_id):
    success = self.mahasiswa_repository.delete_mahasiswa(mahasiswa_id)
    if success:
      return Response(status=204)
    return Response(status=404)
