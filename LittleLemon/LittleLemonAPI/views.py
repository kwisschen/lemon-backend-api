from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from djoser.views import UserViewSet


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})


user_list = UserViewSet.as_view({
    'get': 'list',
})

