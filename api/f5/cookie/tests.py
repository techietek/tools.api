from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class F5CookieTests(APITestCase):
    def test_encode_cookie(self):
        """
        Ensure we get a proper response back
        """
        url = reverse('f5-cookie-decode')
        data = {'encoded_string': '1677687402.36895.0000'}
        response = self.client.post(url, data, format='json')
        response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"ip": "106.122.255.99", "port": "8080", "src": "1677687402.36895.0000"})
