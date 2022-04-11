from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from django.shortcuts import render
from .models import UserUrl
from .serializers import UserUrlSerializer


@api_view(['GET'])
def url_list(request):
    urls = UserUrl.objects.all()
    serializer = UserUrlSerializer(urls, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def short_url(request, uniqueId):
    try:
        url = UserUrl.objects.get(uniqueId=uniqueId)
        return redirect(url.originalUrl)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


def render_react(request):
    return render(request,  template_name="index.html")


@api_view(['POST'])
def gen_short_url(request):
    serializer = UserUrlSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        url_with_redirect = request.build_absolute_uri(
            '/') + "api" + "/urls" + "/" + serializer.data['uniqueId']
        return Response({"url": url_with_redirect}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
