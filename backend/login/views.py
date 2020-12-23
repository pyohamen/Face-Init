from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
class LoginView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': '인증 성공!'}
        return Response(content)