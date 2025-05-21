from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
    def test_index_view_status_code(self):
        """
        Check if the index page returns the right status code
        :return:
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        """
        Check if the index page uses the correct template
        :return:
        """
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")
