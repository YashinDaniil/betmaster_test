from rest_framework import serializers

from wallet_app.models.wallet import WalletHistory
from wallet_app.services.superpay_api import SuperPayApi


class DepositSerializer(serializers.Serializer):
    description = serializers.TextField()
    amount = serializers.DecimalField()
    currency = serializers.TextField()
    merchant_id = serializers.UUIDField()

    def create(self, validated_data):
        super_pay = SuperPayApi()
        deposit_data = super_pay.create_deposit(
            description=validated_data['description'],
            amount=validated_data['amount'],
            currency=validated_data['currency'],
            merchant_id=validated_data['merchant_id'],
        )
        Wallet.objects.get(id=validated_data)
        WalletHistory.objects.create(
            wallet=1,
            merchant=1,
            operation=1,
            operation_id=1,
            operation_status=1,
            operation_description=1,
            created=1,
            amount=1
        )

        # add.delay(4, 4) Запускаем отложенную задачу, если будут долгие ответы

        return 1
