from django.test import TestCase
from django.template.defaultfilters import slugify
from blogsite.models import Post

from wallet_app.models import Wallet, WalletHistory, User


class ModelsTestCase(TestCase):
    def setUp(self):
        self.User1 = User.objects.create(
            name='user1'
        )

        self.Wallet1 = Wallet.objects.create(
            currency='USD',
            deposit_amount=10000.0,
            hold_amount=10000.0,
            withdraw_amount=100.0,
            user=self.User1,
        )

    def some_test(self):
        pass
