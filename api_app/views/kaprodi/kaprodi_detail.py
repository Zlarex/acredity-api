from rest_framework.views import APIView
from rest_framework.response import Response
from ...repositories.kaprodi_repository import KaprodiRepository

class KaprodiDetailAPIView(APIView):
  kaprodi_repository = KaprodiRepository()

  def get(self, request, kaprodi_id):
    kaprodi = self.kaprodi_repository.find_by_id(kaprodi_id)
    if kaprodi is not None:
      return Response(kaprodi)
    return Response(status=404)

  def put(self, request, kaprodi_id):
    success = self.kaprodi_repository.update(kaprodi_id, request.data)
    if success is not None:
      return Response(status=200)
    return Response(status=400)

  def delete(self, request, kaprodi_id):
    success = self.kaprodi_repository.delete(kaprodi_id)
    if success:
      return Response(status=204)
    return Response(status=404)
