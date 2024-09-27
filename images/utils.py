# infoimages/utils.py
from django.http import JsonResponse

def check_api_token(request):
    API_TOKEN = 'a78d3b19-5f24-478e-994b-4b4bff50bb73'
    token = request.headers.get('Authorization')
    if token != API_TOKEN:
        return JsonResponse({'error': 'Invalid token'}, status=403)
    return None  # Token to'g'ri bo'lsa, hech qanday xato yo'q
