from django.test import TestCase

class TestCalls(TestCase):

    def test_index(self):
        response = self.client.get('/', follow=True)
        self.assertEquals(response.status_code, 200)

    def test_fake(self):
        response = self.client.get('/fake', follow=True)
        self.assertEquals(response.status_code, 404)
