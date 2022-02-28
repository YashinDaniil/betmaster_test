from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)


class Wallet(models.Model):
    deposit_amount = models.DecimalField()
    hold_amount = models.DecimalField()
    withdraw_amount = models.DecimalField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    currency = models.CharField(max_length=255)


class WalletHistory(models.Model):
    KIND_OPERATION_PAYMENT = 'payment'
    KIND_OPERATION_PAYOUT = 'payout'

    OPERATION_TYPE_CHOICES = (
        (KIND_OPERATION_PAYMENT, "payment"),
        (KIND_OPERATION_PAYOUT, "payout"),
    )

    KIND_OPERATION_CREATED = 'created'
    KIND_OPERATION_PROCESSING = 'processing'
    KIND_OPERATION_DONE = 'done'
    KIND_OPERATION_REJECTED = 'rejected'

    OPERATIONS_STATUS_CHOICES = (
        (KIND_OPERATION_CREATED, "work"),
        (KIND_OPERATION_PROCESSING, "vacation"),
        (KIND_OPERATION_DONE, "sick"),
        (KIND_OPERATION_REJECTED, "dayoff"),
    )

    wallet = models.ForeignKey(Wallet, on_delete=models.DO_NOTHING)
    merchant = models.UUIDField()
    operation = models.CharField(max_length=128, choices=OPERATION_TYPE_CHOICES)
    operation_status = models.CharField(max_length=128, choices=OPERATIONS_STATUS_CHOICES)
    operation_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=25, decimal_places=10)
    currency = models.CharField(max_length=255)
