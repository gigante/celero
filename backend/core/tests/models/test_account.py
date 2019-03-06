import uuid
from datetime import datetime
from django.test import TestCase
from backend.core.models.account import Account, FlowType


class AccountModelTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            name='Aluguel', currency='2000.00', flow=FlowType.EXPENSE)

    def test_create(self):
        self.assertTrue(Account.objects.exists())

    def test_id_uuid(self):
        self.assertIsInstance(self.account.id, uuid.UUID)

    def test_created_at(self):
        self.assertIsInstance(self.account.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.account.updated_at, datetime)

    def test_str(self):
        self.assertEqual(
            'Aluguel: - R$ 2000.00', str(self.account))
