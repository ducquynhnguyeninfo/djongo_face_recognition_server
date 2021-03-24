from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from order_manager import views

# order_router = DefaultRouter()
# order_router.register('order_manager', OrderViewSet)

urlpatterns = [
    # path('order_manager/', include(order_router.urls)),
    path('brands/', views.BrandList.as_view()),
    path('brands/<str:pk>', views.BrandDetail.as_view()),
    
    path('vehiclemodels/', views.VehicleModelList.as_view()),
    path('vehiclemodels/<str:pk>', views.VehicleModelDetail.as_view()),
    
    path('orders/', views.OrderList.as_view()),
    path('orders/<str:pk>', views.OrderDetail.as_view()),


    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
