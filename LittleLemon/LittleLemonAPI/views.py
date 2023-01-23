from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import MenuItem
from .serializers import MenuItemSerializer, UserSerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


@permission_classes([IsAdminUser])
class ManagersView(generics.ListCreateAPIView):
    queryset = Group.objects.get(name="Manager").user_set.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        if username := request.POST["username"]:
            user = get_object_or_404(User, username=username)
            managers = Group.objects.get(name="Manager")
            managers.user_set.add(user)

            return Response(status.HTTP_201_CREATED)

        return Response({"message": "error"}, status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
class RemoveManagerView(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs["pk"])
        managers = Group.objects.get(name="Manager")
        managers.user_set.remove(user)

        return Response(status.HTTP_200_OK)
