import json
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from backend.core.models.account import Account, FlowType
from backend.core.views import AccountSerializer
from .defaults import ApiMan


class AccountViewTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            name='Aluguel', currency='2000.00', flow=FlowType.EXPENSE)

        # api client with jwt credentials
        apiMan = ApiMan()
        self.client = apiMan.getClientJWT()

    def test_get_all_accounts(self):
        Account.objects.create(
            name='Salario', currency='1200.00', flow=FlowType.RECIPE)
        Account.objects.create(
            name='Mercadinho', currency='45.00', flow=FlowType.EXPENSE)

        # get API response
        api_route = reverse('account-list')
        response = self.client.get(api_route)

        # get data from db
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)

        # asserts
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_account(self):
        # get API response
        api_route = reverse('account-detail', kwargs={'pk': self.account.id})
        response = self.client.get(api_route)

        # get one account
        account = Account.objects.get(pk=self.account.id)
        serializer = AccountSerializer(account)

        # asserts
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_account(self):
        # get invalid account
        api_route = reverse('account-detail', kwargs={'pk': 53})
        response = self.client.get(api_route)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_account(self):
        valid_payload = {
            'name': 'Aluguel',
            'currency': '3200',
            'flow': FlowType.EXPENSE
        }

        response = self.client.post(
            reverse('account-list'),
            data=json.dumps(valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_account(self):
        invalid_payload = {
            'name': 'Aluguel',
            'currency': '3200',
            'flow': 'FLW'
        }

        response = self.client.post(
            reverse('account-list'),
            data=json.dumps(invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update(self):
        valid_payload = {
            'name': 'Aluguel',
            'currency': '1200.00',
            'flow': FlowType.EXPENSE
        }

        response = self.client.put(
            reverse('account-detail', kwargs={'pk': self.account.id}),
            data=json.dumps(valid_payload),
            content_type='application/json')

        self.assertIn(response.status_code,
                      [status.HTTP_204_NO_CONTENT, status.HTTP_200_OK])

    def test_invalid_update(self):
        valid_payload = {
            'name': 'Aluguel',
            'currency': '1200.00',
            'flow': 'FLW'
        }

        response = self.client.put(
            reverse('account-detail', kwargs={'pk': self.account.id}),
            data=json.dumps(valid_payload),
            content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
