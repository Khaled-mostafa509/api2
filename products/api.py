from .models import Home , Category
from .serializers import HomeSerializers , CategorySerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET','Post'])

def Home_listAPI(request):
    all_ads=Home.objects.all()
    data=HomeSerializers(all_ads,many=True).data
    return Response({'data':data})
@api_view(['GET','POST'])
def Category_list(request):
    all_category= Category.objects.all()
    data=CategorySerializers(all_category,many=True).data
    return Response({'data':data})