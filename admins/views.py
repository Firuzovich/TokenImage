from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from images.models import BarcodeData

class ImagesManageView(APIView):
    """
    API to manage images for admin panel.
    """
    permission_classes = [IsAdminUser]  # Faqat admin foydalanuvchilar uchun

    def get(self, request):
        # Barcha ma'lumotlarni olish
        images = BarcodeData.objects.all()
        data = []
        for image in images:
            data.append({
                'id': image.id,
                'barcode': image.barcode,
                'date': image.date,
                'fish': image.fish,
                'region': image.region.name,
                'district': image.district.name,
                'post_name': image.post_name,
                'photo': image.photo.url if image.photo else None
            })
        return Response(data, status=status.HTTP_200_OK)

    # def delete(self, request, pk):
    #     # ID bo'yicha ma'lumotni o'chirish
    #     try:
    #         image = BarcodeData.objects.get(pk=pk)
    #         image.delete()
    #         return Response({'message': 'Image deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    #     except BarcodeData.DoesNotExist:
    #         return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)
