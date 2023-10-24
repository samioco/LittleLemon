from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer


# @api_view(['POST']) # wrapped to use Response class
# def books(request):
#   return Response('list of the books', status=status.HTTP_200_OK)

# def index(request):
#   return render(request, 'index.html', {})

@api_view()
@permission_classes([IsAuthenticated])
def securedview(request):
  return Response({"message": "authentication successful"})

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]
  
class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticated]
  
class MenuItemView(ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer
  
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer
  
