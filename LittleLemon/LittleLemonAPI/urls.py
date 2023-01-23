from django.urls import path

from . import views

urlpatterns = [
    path("menu-items", views.MenuItemsView.as_view()),
    path("menu-items/<int:pk>", views.MenuItemView.as_view()),
    path("groups/manager/users", views.ManagersView.as_view()),
    path("groups/manager/users/<int:pk>", views.RemoveManagerView.as_view()),
    path("groups/delivery-crew/users", views.DeliveryCrewView.as_view()),
    path("groups/delivery-crew/users/<int:pk>", views.RemoveDeliveryCrewView.as_view()),
    # path("cart/menu-items", ),
    # path("cart/orders", ),
    # path("cart/orders/<int:pk>", ),
]
