from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from ...repositories.kaprodi_repository import KaprodiRepository

class KaprodiListAPIView(APIView):
  kaprodi_repository = KaprodiRepository()

  def get(self, request):
    kaprodi = self.kaprodi_repository.find_all()
    return Response(kaprodi)

  def post(self, request):
    kaprodi_id = self.kaprodi_repository.create(request.data)
    if kaprodi_id is not None:
      return Response({'id': kaprodi_id}, status=201)
    return Response(status=400)