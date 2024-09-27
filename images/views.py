from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.conf import settings
from .models import BarcodeData, Region, District
from .utils import check_api_token 

class BarcodeDataView(APIView):
    """
    API to save barcode data, requires a static token.
    """

    def post(self, request):
        # Tokenni tekshirish
        token_error = check_api_token(request)
        if token_error:
            return token_error

        # Kiritilgan ma'lumotlarni olish
        data = request.data
        barcode = data.get('barcode')
        fish = data.get('fish')
        region_name = data.get('region')
        district_name = data.get('district')
        post_name = data.get('post_name')
        photo = request.FILES.get('photo')

        # Majburiy maydonlarni tekshirish
        if not barcode or not fish or not region_name or not district_name or not post_name or not photo:
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        # Date kiritilgan yoki yo'qligini tekshirish
        date = data.get('date')
        if not date:
            date = timezone.now()

        # Region va Districtni tekshirish yoki yaratish
        try:
            region, _ = Region.objects.get_or_create(name=region_name)
            district, _ = District.objects.get_or_create(name=district_name, region=region)

            # Ma'lumotlarni saqlash
            barcode_data = BarcodeData.objects.create(
                barcode=barcode,
                date=date,
                fish=fish,
                region=region,
                district=district,
                post_name=post_name,
                photo=photo
            )

            return Response({'message': 'Data saved successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
