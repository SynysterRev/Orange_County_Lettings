from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from profiles.models import Profile


class IndexViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test123")
        self.profile = Profile.objects.create(user=self.user, favorite_city="BugCity")

    def test_index_view_status_code(self):
        """
        Check that the index page of the users profiles returns a 200 status code.
        """
        response = self.client.get(reverse("profiles_index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("Profiles", response.content.decode())

    def test_index_view_uses_correct_template(self):
        """
        Check that the index page of the users profiles uses the correct template.
        """
        response = self.client.get(reverse("profiles_index"))
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_profile_view_status_code(self):
        """
        Check that the profile page of a specific user returns a 200 status code and
        correspond to the user.
        """
        response = self.client.get(
            reverse("profile", kwargs={"username": self.user.username}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.profile.user.username, response.content.decode())

    def test_profile_view_uses_correct_template(self):
        """
        Check that the profile page of a specific user uses the correct template.
        """
        response = self.client.get(
            reverse("profile", kwargs={"username": self.user.username}))
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_profile_view_incorrect_username(self):
        """
        Check that an incorrect username raises an error 404.
        """
        response = self.client.get(reverse("profile", kwargs={"username": "false"}))
        self.assertEqual(response.status_code, 404)

    def test_profile_view_incorrect_username_template(self):
        """
        Check that an incorrect username display the correct template.
        """
        response = self.client.get(reverse("profile", kwargs={"username": "false"}))
        self.assertTemplateUsed(response, "404.html")

    def test_create_user(self):
        """
        Check that the user creation is successful.
        """
        user = User.objects.create_user(username="test2", password="test123",
                                        first_name="test", last_name="test")
        self.assertEqual(user.username, "test2")
        self.assertEqual(user.first_name, "test")
        self.assertEqual(user.last_name, "test")

    def test_create_profile(self):
        """
        Check that the profile creation is successful.
        """
        user = User.objects.create_user(username="test2", password="test123")
        profile = Profile.objects.create(user=user, favorite_city="TestCity")
        self.assertEqual(profile.favorite_city, "TestCity")
        self.assertEqual(profile.user, user)
        self.assertEqual(str(profile), "test2")
