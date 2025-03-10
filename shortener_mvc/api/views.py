# api/views.py

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import URL
from django.http import JsonResponse

url_param = openapi.Parameter('original_url', openapi.IN_BODY, description="Original URL to shorten", type=openapi.TYPE_STRING, required=True)
response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'url': openapi.Schema(type=openapi.TYPE_STRING),
    }
)
error_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'error': openapi.Schema(type=openapi.TYPE_STRING),
    }
)

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['original_url'],
        properties={
            'original_url': openapi.Schema(type=openapi.TYPE_STRING)
        },
    ),
    responses={
        201: response_schema,
        400: error_response_schema,
        405: error_response_schema,
        500: error_response_schema,
    }
)
@api_view(['POST'])
def create(request, admin_url = ''):
    original_url = request.data.get('original_url')
    if not original_url:
        return Response({'error': 'Original URL is required'}, status=400)
    
    try:
        if admin_url:
            url = URL(admin_token=admin_url, original_url=original_url)
        else:
            url = URL(original_url=original_url)
        url.save()
        return Response(
            {
                'url': str(url),
                'short_code': url.short_code,
                'short_url': url.get_absolute_url(),
                'admin_token': url.admin_token
            }, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

    
@swagger_auto_schema(method='get')
def list(request):
    pass

@swagger_auto_schema(method='get')
def info(request):
    pass

@swagger_auto_schema(method='get')
def stats(request):
    pass

@swagger_auto_schema(method='put')
def update(request):
    pass

@swagger_auto_schema(method='delete')
def delete(request):
    pass