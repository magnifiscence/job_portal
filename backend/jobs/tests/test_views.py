import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Job, Company
from ..serializers import JobSerializer
from django.contrib.auth.models import User

import datetime

# initialize the APIClient app
client = APIClient()


class GellAllJobsTest(TestCase):
    """ Test module for GET all jobs API """

    def setUp(self):
        company = Company.objects.create(
            name="Company X",
        )
        company2 = Company.objects.create(
            name="Company Y",
        )

        Job.objects.create(
            title="Test Job",
            salaray=1000,
            description="Test Description",
            experiance=10,
            datestamp=datetime.datetime.now(),
            company=company,
        )
        Job.objects.create(
            title="Test Job 2",
            salaray=1000,
            description="Test Description",
            experiance=3,
            datestamp=datetime.datetime.now(),
            company=company2
        )

        Job.objects.create(
            title="Test Job 3",
            salaray=1000,
            description="Test Description",
            experiance=10,
            datestamp=datetime.datetime.now(),
            company=company,
        )

        Job.objects.create(
            title="Test Job",
            salaray=1000,
            description="Test Description",
            experiance=10,
            datestamp=datetime.datetime.now(),
            company=company2,
        )

    def test_get_all_jobs(self):
        # get API response
        response = client.get('/jobs/')
        # get data from db
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GellSingleJobTest(TestCase):
    """ Test module for GET single job API """

    def setUp(self):
        company = Company.objects.create(
            name="Company X",
        )
        company2 = Company.objects.create(
            name="Company Y",
        )

        self.job1 = Job.objects.create(
            title="Test Job",
            salaray=1000,
            description="Test Description",
            experiance=10,
            datestamp=datetime.datetime.now(),
            company=company,
        )
        self.job2 = Job.objects.create(
            title="Test Job 2",
            salaray=1000,
            description="Test Description",
            experiance=3,
            datestamp=datetime.datetime.now(),
            company=company2
        )

        self.job3 = Job.objects.create(
            title="Test Job 3",
            salaray=1000,
            description="Test Description",
            experiance=10,
            datestamp=datetime.datetime.now(),
            company=company,
        )

        self.job4 = Job.objects.create(
            title="Test Job",
            salaray=1000,
            description="Test Description",
            experiance=10,
            datestamp=datetime.datetime.now(),
            company=company2,
        )

    def test_get_valid_single_job(self):
        pk = self.job1.pk
        response = client.get('/jobs/{}/'.format(pk))
        job = Job.objects.get(pk=pk)
        serializer = JobSerializer(job)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_job(self):
        response = client.get('/jobs/99/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateSingleJobTest(TestCase):
    """ Test module for updating an existing Job record """

    def setUp(self):
        User.objects.create_user(username="test")
        company = Company.objects.create(
            name="Company X",
        )
        company2 = Company.objects.create(
            name="Company Y",
        )

        self.job1 = Job.objects.create(
            title="Test Job",
            salaray=1000,
            description="Test Description",
            experiance=10,
            datestamp=datetime.datetime.now(),
            company=company,
        )
        pk = self.job1.pk
        self.valid_payload = client.get('/jobs/{}/'.format(pk))

    def test_valid_update_Job(self):
        user = User.objects.get(username='test')
        client.force_authenticate(user=user)
        pk = self.job1.pk
        response = client.patch(
            '/jobs/{}/'.format(pk),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.patch(
            '/jobs/{}/'.format(pk),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauth_update_Job(self):
        pk = self.job1.pk
        response = client.patch(
            '/jobs/{}/'.format(pk),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)