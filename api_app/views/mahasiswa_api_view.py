from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..repositories.mahasiswa_repository import MahasiswaRepository
from ..permissions.kaprodi_permission import KaprodiPermission
from ..serializers.mahasiswa_serializer import MahasiswaSerializer

class MahasiswaListAPIView(APIView):
  mahasiswa_repository = MahasiswaRepository()

  def get(self, request):
    mahasiswa = self.mahasiswa_repository.find_all()
    return Response(MahasiswaSerializer(mahasiswa, many=True).data)

  def post(self, request):
    permission_classes = [IsAuthenticated, KaprodiPermission]
    mahasiswa_id = self.mahasiswa_repository.create(request.data)
    if mahasiswa_id is not None:
      return Response({'id': mahasiswa_id}, status=201)
    return Response(status=400)
  
class MahasiswaDetailAPIView(APIView):
  mahasiswa_repository = MahasiswaRepository()

  def get(self, request, nim):
    mahasiswa = self.mahasiswa_repository.find_by_nim(nim)
    if mahasiswa is not None:
      return Response(MahasiswaSerializer(mahasiswa).data)
    return Response(status=404)

  def put(self, request, nim):
    permission_classes = [IsAuthenticated, KaprodiPermission]
    success = self.mahasiswa_repository.update(nim, request.data)
    if success is not None:
      return Response(status=200)
    return Response(status=400)

  def delete(self, request, nim):
    permission_classes = [IsAuthenticated, KaprodiPermission]
    success = self.mahasiswa_repository.delete(nim)
    if success:
      return Response(status=204)
    return Response(status=404)
