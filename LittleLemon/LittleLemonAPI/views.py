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

    def post(self, request, *args, **kwargs):
        if (
            request.user.is_anonymous
            or not request.user.groups.filter(name="Manager").exists()
        ):
            return Response(status.HTTP_403_FORBIDDEN)

        return super().post(request, *args, **kwargs)


class MenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != "GET":
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


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


@permission_classes([IsAdminUser])
class DeliveryCrewView(generics.ListCreateAPIView):
    queryset = Group.objects.get(name="Delivery crew").user_set.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        if username := request.POST["username"]:
            user = get_object_or_404(User, username=username)
            managers = Group.objects.get(name="Delivery crew")
            managers.user_set.add(user)

            return Response(status.HTTP_201_CREATED)

        return Response({"message": "error"}, status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUser])
class RemoveDeliveryCrewView(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs["pk"])
        managers = Group.objects.get(name="Delivery crew")
        managers.user_set.remove(user)

        return Response(status.HTTP_200_OK)
