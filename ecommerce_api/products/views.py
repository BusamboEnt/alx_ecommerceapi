from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, filters
from .models import User, Product, Order, OrderItem
from .serializers import UserSerializer, ProductSerializer, OrderSerializer, OrderItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category']
    
    
    def get_permissions(self):
        if self.request.method in ['GET']:
            return [AllowAny()]
        return [IsAuthenticated()]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Show only orders belonging to the logged-in user
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Auto-assign the user to the order on creation
        serializer.save(user=self.request.user)
