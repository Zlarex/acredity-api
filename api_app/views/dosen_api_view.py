from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from ..repositories.dosen_repository import DosenRepository
from ..serializers.dosen_serializer import DosenSerializer
from ..permissions.kaprodi_permission import KaprodiPermission

class DosenAPIView(APIView):
  permission_classes = [KaprodiPermission]
  dosen_repository = DosenRepository()

  class Meta:
    abstract=True

class DosenListAPIView(DosenAPIView):
  def get(self, request):
    dosen_list = self.dosen_repository.find_all()
    return Response(DosenSerializer(dosen_list, many=True).data)
  
  def post(self, request):
    dosen_id = self.dosen_repository.create(request.data)
    if dosen_id is not None:
      return Response({'id': dosen_id}, status=201)
    return Response(status=400)

class DosenDetailAPIView(DosenAPIView):
  def get(self, request, nip):
    dosen = self.dosen_repository.find_by_nip(nip)
    if dosen is not None:
      return Response(DosenSerializer(dosen).data)
    return Response(status=404)


  def put(self, request, nip):
    success = self.dosen_repository.update(nip, request.data)
    if success is not None:
      return Response(status=200)
    return Response(status=400)

  def delete(self, request, nip):
    success = self.dosen_repository.delete(nip)
    if success:
      return Response(status=204)
    return Response(status=404)

class DosenLoginAPIView(DosenAPIView):
  permission_classes = []
  def post(self, request):
    nip = request.data.get('nip')
    password = request.data.get('password')

    dosen = self.dosen_repository.find_by_nip(nip=nip)
    if dosen is not None and dosen.check_password(password):
      refresh = RefreshToken.for_user(dosen)
      serializer = DosenSerializer(dosen)
      return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'user': serializer.data}, status=200)
    else:
      return Response(status=400)