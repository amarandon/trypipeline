from django.test import TestCase

# Create your tests here.
class TestHome(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertContains(response, 'css')
