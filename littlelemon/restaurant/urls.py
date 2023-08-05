from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('tables', views.BookingViewSet)

urlpatterns = [
    path('menu-items', views.MenuView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuView.as_view()),
    path('booking/', include(router.urls)),
    path('message', views.msg),
    path('api-token-auth/', obtain_auth_token),
]