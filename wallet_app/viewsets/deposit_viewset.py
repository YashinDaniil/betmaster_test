from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from wallet_app.models import Wallet
from rest_framework.response import Response
from rest_framework import status


class DepositViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_classes = {
        'create': SpecApplicationCreateSerializer,
        'list': SpecApplicationCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def get_queryset(self):
        return Wallet.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=status.HTTP_201_CREATED)
