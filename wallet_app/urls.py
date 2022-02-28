from django.urls import path, include
from rest_framework import routers

from wallet_app.viewsets import WalletViewSet, PayoutViewSet

wallet_route = routers.DefaultRouter()
wallet_route.register('wallet', WalletViewSet, basename='WalletViewSet')

wallet_route = routers.DefaultRouter()
wallet_route.register('payout', PayoutViewSet, basename='PayoutViewSet')

urlpatterns = [
    path('', include(wallet_route.urls)),
]
