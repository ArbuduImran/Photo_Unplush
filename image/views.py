import requests
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Photo
from .serializers import PhotoSerializer


class PhotoSearchView(APIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, keyword):
        api_key = 'V93q2Wkj7o2bbPNEabw3b0Y3esdVV31pJMpQYbBo4hU  '
        url = 'https://api.unsplash.com/photos/random'

        headers = {
            'Authorization': f'Client-ID {api_key}'
        }

        params = {
            'query': keyword
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        photo_data = {
            'keyword': keyword,
            'image_url': data['urls']['regular']
        }

        serializer = self.serializer_class(data=photo_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

