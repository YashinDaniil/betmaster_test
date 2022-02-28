import json
import uuid

import data as data
import requests
import total as total
from decouple import config

from wallet_app.schemas import DepositSuperPaySchema, PayoutSuperPaySchema, StatusSuperPaySchema, CallbackMetaSchema


class SuperPayApi:
    def __init__(
            self,
            superpay_host: str = config('superpay_host', cast=str),
            superpay_email: str = config('superpay_email', cast=str),
            public_key: str = config('public_key', cast=str),
            superpay_pass: str = config('superpay_pass', cast=str),
    ):
        self.superpay_host = superpay_host
        self.public_key = public_key
        self.superpay_email = superpay_email
        self.superpay_pass = superpay_pass

        request = requests.post(
            '{},{}'.format(superpay_host, 'autorization/'),
            json={'email': superpay_email, 'pass': superpay_pass})

        self.headers = json.loads(request.text)['authorization_token']

        self.redirect_url = {
            'success_url': config('success_url', cast=str),
            'failure_url': config('failure_url', cast=str),
        }


    def get_payout(self, description: str, amount: float, currency: str, wallet_id: uuid, merchant_id: uuid) -> PayoutSuperPaySchema:
        request = requests.post(
            '{}/{}'.format(self.superpay_host, 'payout'),
            json={
                'description': description,
                'amount': amount,
                'currency': currency,
                'wallet_id': wallet_id,
                'merchant_id': merchant_id
            },
            header=self.headers)

        data = json.loads(request.text)

        return PayoutSuperPaySchema(
            wallet_id=data['wallet_id'],
            merchant_id=data['merchant_id'],
            operation_time=data['operation_time'],
            operation_success=data['operation_success'],
            operation_description=data['operation_description']
        )


    def get_callback(self, merchant_id: uuid, filters_reference: str, filter_status:  str) -> StatusSuperPaySchema:
        filters_param = ''
        if filters_reference:
            filters_param += 'filter_reference=' + filters_reference

        if filter_status:
            filters_param += 'filter_status=' + str(filter_status)


        request = requests.get('{}/{}/{}'.format(self.superpay_host, 'deposit/status', str(merchant_id)),  params=filters_param, headers=self.headers)
        data = json.loads(request.text)
        return StatusSuperPaySchema(
            meta=CallbackMetaSchema(
                total=data['meta']['total'],
                pages=data['meta']['pages'],
                page=data['meta']['page']
            ),
            id=data['id'],
            status=data['status'],
            status_detail=data['status_detail'],
            attempt=data['attempt'],
            max_attempt=data['max_attempt'],
            created=data['created'],
            progresses=data['progress'],
            merchant_id=data['merchant_id'],
            operation_time=data['operation_time'],
            operation_success=data['operation_success'],
            operation_description=data['operation_description']
        )

    def create_deposit(self, description: str, amount: float, currency: str,  merchant_id:uuid) -> DepositSuperPaySchema:
        request = requests.post(
            '{}/{}'.format(self.superpay_host, 'payout'),
            json={
                'description': description,
                'amount': amount,
                'currency': currency,  # USD, RUB, EUR
                'redirect_success_url': self.redirect_url['success_url'],
                'redirect_failure_url': self.redirect_url['failure_url'],
                'merchant_id': merchant_id,
                'public_key': self.public_key  # Add new key
            },
            header=self.headers)

        data = json.loads(request.text)

        return DepositSuperPaySchema(
            merchant_id=data['merchant_id'],
            operation_time=data['operation_time'],
            operation_success=data['operation_success'],
            operation_description=data['operation_description']
        )