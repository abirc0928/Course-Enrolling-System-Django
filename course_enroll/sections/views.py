from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.
# class SectionView(APIView):
#     def post(self, request):
#         section = Sections(
#             course=Course.objects.get(id=request.data["course_id"]),
#             section_name=request.data["section_name"],
#             schedule=request.data["schedule"],
#             capacity=request.data["capacity"],
#         )
#         section.save()
#         return Response(status=status.HTTP_201_CREATED)
        

class SectionViewSet(ModelViewSet):
    queryset = Sections.objects.all()
    serializer_class = SectionSerializer