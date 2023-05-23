from rest_framework.views import APIView
from rest_framework.response import Response
from ..repositories.kaprodi_repository import KaprodiRepository

class KaprodiListAPIView(APIView):
  kaprodi_repository = KaprodiRepository()

  def get(self, request):
    kaprodi = self.kaprodi_repository.find_all()
    return Response(kaprodi)

class KaprodiDetailAPIView(APIView):
  kaprodi_repository = KaprodiRepository()

  def get(self, request, nip):
    kaprodi = self.kaprodi_repository.find_by_nip(nip)
    if kaprodi is not None:
      return Response(kaprodi)
    return Response(status=404)

  def post(self, request):
    kaprodi_id = self.kaprodi_repository.create(request.data)
    if kaprodi_id is not None:
      return Response({'id': kaprodi_id}, status=201)
    return Response(status=400)

  def put(self, request, nip):
    success = self.kaprodi_repository.update(nip, request.data)
    if success is not None:
      return Response(status=200)
    return Response(status=400)

  def delete(self, request, nip):
    success = self.kaprodi_repository.delete(nip)
    if success:
      return Response(status=204)
    return Response(status=404)
