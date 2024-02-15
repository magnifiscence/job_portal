from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Profile
import datetime


class ProfileModelTests(TestCase):
    def setUp(self):
        user = User.objects.create(username="test")
        user.profile.bio = "test bio"
        user.profile.location = "test location"
        user.profile.education = "test education"
        user.profile.experiance = "test experiance"
        user.profile.birth_date = datetime.datetime.now()
        user.profile.save()

    def test_profile(self):
        user = User.objects.get(username="test")
        profile = Profile.objects.get(user=user)
        self.assertEqual(str(profile), user.username)
        self.assertEqual(str(user), user.username)
        self.assertEqual(user.profile.bio, "test bio")
        self.assertEqual(user.profile.location, "test location")
        self.assertEqual(user.profile.education, "test education")
        self.assertEqual(user.profile.experiance, "test experiance"