from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('orderitems', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api,token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
