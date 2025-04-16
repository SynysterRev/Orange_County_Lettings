from django.test import TestCase
from django.urls import reverse

from lettings.models import Letting, Address


class IndexViewTests(TestCase):
    def setUp(self):
        self.address = Address.objects.create(number=10, street="Boulevard",
                                              city="Paris", state="France",
                                              zip_code="12345", country_iso_code="FR")
        self.letting = Letting.objects.create(title='Test Letting',
                                              address=self.address)

    def test_index_view_status_code(self):
        """
        Check that the index page of the lettings returns a 200 status code.
        """
        response = self.client.get(reverse("lettings_index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("Lettings", response.content.decode())

    def test_index_view_uses_correct_template(self):
        """
        Check that the index page of the lettings uses the correct template.
        """
        response = self.client.get(reverse("lettings_index"))
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_letting_view_status_code(self):
        """
        Check that the letting page of a specific letting returns a 200 status code and
        correspond to it.
        """
        response = self.client.get(
            reverse("letting", kwargs={"letting_id": self.letting.id}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.letting.title, response.content.decode())

    def test_letting_view_uses_correct_template(self):
        """
        Check that the letting page of a specific letting uses the correct template.
        """
        response = self.client.get(
            reverse("letting", kwargs={"letting_id": self.letting.id}))
        self.assertTemplateUsed(response, "lettings/letting.html")

    def test_letting_view_incorrect_id(self):
        """
        Check that an incorrect letting id raises an error 404.
        """
        response = self.client.get(reverse("letting", kwargs={"letting_id": 130}))
        self.assertEqual(response.status_code, 404)

    def test_letting_view_incorrect_id_template(self):
        """
        Check that an incorrect letting id display the correct template.
        """
        response = self.client.get(reverse("letting", kwargs={"letting_id": 130}))
        self.assertTemplateUsed(response, "404.html")

    def test_create_address(self):
        """
        Check that the address creation is successful.
        """
        address = Address.objects.create(number=10, street="Boulevard",
                                         city="Paris", state="France",
                                         zip_code="12345", country_iso_code="FR")
        self.assertEqual(address.number, 10)
        self.assertEqual(address.street, "Boulevard")
        self.assertEqual(address.city, "Paris")
        self.assertEqual(address.state, "France")
        self.assertEqual(address.zip_code, "12345")
        self.assertEqual(address.country_iso_code, "FR")
        self.assertEqual(str(address), "10 Boulevard")

    def test_create_letting(self):
        """
        Check that the letting creation is successful.
        """
        address = Address.objects.create(number=12, street="Boulevard",
                                         city="Paris", state="France",
                                         zip_code="12345", country_iso_code="FR")
        letting = Letting.objects.create(title="letting", address=address)
        self.assertEqual(letting.title, "letting")
        self.assertEqual(letting.address, address)
        self.assertEqual(str(letting), "letting")
