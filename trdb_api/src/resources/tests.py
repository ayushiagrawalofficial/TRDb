from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from rest_framework import test, status
from rest_framework.authtoken.models import Token

from resources.apps import ResourcesConfig
from resources.models import Technology

User = get_user_model()


class TestTechnologyAPI(test.APITestCase):
    """Test Technology API"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username="tester", password="bar")
        cls.token = Token.objects.create(user=cls.user)
        cls.payload = {"technology_type": Technology.Type.LANGUAGE, "name": "Python"}

    @classmethod
    def tearDownClass(cls):
        cls.token.delete()
        cls.user.delete()
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def tearDown(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=None)
        super().tearDown()

    def test_list_api(self):
        url = reverse(":".join([ResourcesConfig.name, "technology-list"]))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_api(self):
        url = reverse(":".join([ResourcesConfig.name, "technology-list"]))
        response = self.client.post(url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_api(self):
        kwargs = self.payload
        kwargs["user"] = self.user
        instance = Technology.objects.create(**kwargs)
        url = reverse(
            ":".join([ResourcesConfig.name, "technology-detail"]), args=[instance.id]
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_api(self):
        kwargs = self.payload.copy()
        kwargs["user"] = self.user
        instance = Technology.objects.create(**kwargs)
        payload = self.payload.copy()
        payload["user"] = self.user.id
        payload["name"] = "java"
        url = reverse(
            ":".join([ResourcesConfig.name, "technology-detail"]), args=[instance.id]
        )
        response = self.client.put(url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pass_destroy(self):
        kwargs = self.payload
        kwargs["user"] = self.user
        instance = Technology.objects.create(**kwargs)
        url = reverse(
            ":".join([ResourcesConfig.name, "technology-detail"]), args=[instance.id]
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestStudyResourceAPI(test.APITestCase):
    """Test Study Resource API"""

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

    def tearDown(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=None)
        super().tearDown()

    def test_list_api(self):
        url = reverse(":".join([ResourcesConfig.name, "study-resource-list"]))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestVoteAPI(test.APITestCase):
    """Test Vote API"""

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

    def tearDown(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=None)
        super().tearDown()

    def test_list_api(self):
        url = reverse(":".join([ResourcesConfig.name, "vote-list"]))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
