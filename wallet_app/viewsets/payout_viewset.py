from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from wallet_app.models import Wallet


class PayoutViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_classes = {
        'create': SpecApplicationCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def get_queryset(self):
        return Wallet.objects.all()
