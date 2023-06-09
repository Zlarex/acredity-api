from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from ..repositories.kaprodi_repository import KaprodiRepository
from ..serializers.kaprodi_serializer import KaprodiSerializer

class KaprodiAPIView(APIView):
  kaprodi_repository = KaprodiRepository()

  class Meta:
    abstract=True

class KaprodiListAPIView(KaprodiAPIView):
  def get(self, request):
    kaprodi_list = self.kaprodi_repository.find_all()
    return Response(KaprodiSerializer(kaprodi_list, many=True).data)
  
  def post(self, request):
    kaprodi_id = self.kaprodi_repository.create(request.data)
    if kaprodi_id is not None:
      return Response({'id': kaprodi_id}, status=201)
    return Response(status=400)

class KaprodiDetailAPIView(KaprodiAPIView):
  def get(self, request, nip):
    kaprodi = self.kaprodi_repository.find_by_nip(nip)
    if kaprodi is not None:
      return Response(KaprodiSerializer(kaprodi).data)
    return Response(status=404)


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

class KaprodiLoginAPIView(KaprodiAPIView):
  def post(self, request):
    nip = request.data.get('nip')
    password = request.data.get('password')

    kaprodi = self.kaprodi_repository.find_by_nip(nip=nip)
    if kaprodi is not None and kaprodi.check_password(password):
      refresh = RefreshToken.for_user(kaprodi)
      serializer = KaprodiSerializer(kaprodi)
      return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'user': serializer.data}, status=200)
    else:
      return Response(status=400)