from .models import Image, Text
from .serializers import ImageSerializer, TextSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils.for_conversion import get_img

# Create your views here.
@api_view(('POST',))
def convert_image(request):
    '''
    for download the image, convert it to text and save text to database
    '''
    text = get_img(request.data['url'], request.data['name'])
    new_text = Text(text=text)
    new_text.save()
    image = Image(url='media/' + request.data['name'])
    image.save()
    serializer = TextSerializer(new_text)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(('GET',))
def get_text(request):
    '''
    for get text from database and return it
    '''
    try:
        texts = Text.objects.all()
        serializer = TextSerializer(texts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)

@api_view(('GET',))
def get_images(request):
    '''
    for get url images from database and return it
    (django will serve the image for visualization)
    '''
    try:
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)


