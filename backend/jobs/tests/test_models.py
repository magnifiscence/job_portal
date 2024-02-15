from django.test import TestCase
from ..models import Job, Qualification, Location, Category, Company

import datetime


class JobTest(TestCase):
    """ Test module for Job Model """

    def setUp(self):
        Job.objects.create(
            title="Test Job",
            salaray=1000,
            description="Test Description",
            experiance=10,
            datestamp=datetime.datetime.now(),
            company=Company.objects.create(
                name="Company X",
            ),
        )

    def test_string_representation(self):
        job = Job.objects.get(title="Test Job")
        self.assertEqual(str(job), job.title)

    def test_created_properly(self):
        job = Job.objects.get(title="Test Job")
        self.assertEqual(job.title, "Test Job")
        self.assertEqual(job.salaray, 1000)
        self.assertEqual(job.description, "Test Description")
        self.assertEqual(True, job.company in Company.objects.all())
        self.assertEqual(job.company.name, "Company X")


class CompanyTest(TestCase):
    """ Test module for Company Model """

    def setUp(self):
        Company.objects.create(
            name="Company X",
        )

    def test_string_representation(self):
        company = Company.objects.get(name="Company X")
        self.assertEqual(str(company), company.name)

    def test_created_properly(self):
        company = Company.objects.get(name="Company X")
        self.assertEqual(company.name, "Company X")


class LocationTest(TestCase):
    """ Test module for Location Model """

    def setUp(self):
        Location.objects.create(
            name="Location X",
        )

    def test_string_representation(self):
        location = Location.objects.get(name="Location X")
        self.assertEqual(str(location), location.name)

    def test_created_properly(self):
        location = Location.objects.get(name="Location X")
        self.assertEqual(location.name, "Location X")


class QualificationTest(TestCase):
    """ Test module for Qualification Model """

    def setUp(self):
        Qualification.objects.create(
            name="Qualification X",
        )

    def test_string_representation(self):
        qualification = Qualification.objects.get(name="Qualification X")
        self.assertEqual(str(qualification), qualification.name)

    def test_created_properly(self):
        qualification = Qualification.objects.get(name="Qualification X")
        self.assertEqual(qualification.name, "Qualification X")


class CategoryTest(TestCase):
    """ Test module for Category Model """

    def setUp(self):
        Category.objects.create(
            name="Category X",
        )

    def test_string_representation(self):
        category = Category.objects.get(name="Category X")
        self.assertEqual(str(category), category.name)

    def test_created_properly(self):
        category = Category.objects.get(name="Category X")
        self.assertEqual(category.name, "Category X")