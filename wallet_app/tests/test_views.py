from django.test import TestCase, Client
from django.urls import reverse

from wallet_app.models import Wallet, User


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client(),
        self.wallet_url = 'v1/wallet/'
        user = User.objects.create(name='user')
        self.wallet1 = Wallet.objects.create(
            deposit_amount=1000.0,
            hold_amount=100.0,
            withdraw_amount=1000.0,
            user = user,
            currency='USD'
        )

    def test_wallet_history_GET(self):
        response = self.client.get(reverse(self.wallet_url))
        self.assertEqual(response.status_code, 200)

    def test_wallet_history_POST(self):
        response = self.client.post(reverse(self.wallet_url), {'some_date'})
        self.assertEqual(response.status_code, 201)
