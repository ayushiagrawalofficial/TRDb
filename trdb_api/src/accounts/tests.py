from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from rest_framework import test, status
from rest_framework.authtoken.models import Token

from accounts.apps import AccountsConfig

User = get_user_model()


class TestLoginAPI(test.APITestCase):
    """Test Login API"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username="tester", password="bar")

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        super().tearDownClass()

    def test_login(self):
        """Login user."""
        url = reverse(":".join([AccountsConfig.name, "login"]))
        payload = {"username": "tester", "password": "bar"}
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestAccountAPI(test.APITestCase):
    """Test Account API"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username="tester", password="bar")
        cls.token = Token.objects.create(user=cls.user)

    @classmethod
    def tearDownClass(cls):
        cls.token.delete()
        cls.user.delete()
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_detail_api(self):
        """Get user detail."""
        url = reverse(":".join([AccountsConfig.name, "detail"]))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout_api(self):
        """Logout user."""
        url = reverse(":".join([AccountsConfig.name, "logout"]))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
