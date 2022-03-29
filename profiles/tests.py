from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from locations import models as locations


class UserRegistrationTestCase(APITestCase):
    def test_correct_registration(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 1,
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_with_empty_username(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 1,
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_without_username(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 1,
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_empty_password(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 1,
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_without_password(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 1,
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_empty_email(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 1,
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_without_email(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 1,
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_empty_first_name(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "",
            "last_name": "last_name",
            "country": 1,
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_without_first_name(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "last_name": "last_name",
            "country": 1,
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_empty_last_name(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "",
            "country": 1,
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_without_last_name(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "country": 1,
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_empty_country(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": "",
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_without_country(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_empty_city(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 1,
            "city": "",
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_without_city(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_empty_credit(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 1,
            "city": 1,
            "credit": "",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_without_credit(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 1,
            "city": 1,
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_invalid_country(self):
        locations.Country.objects.create(country="egypt")
        locations.City.objects.create(country_id=1, city="cairo")
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 2,
            "city": 1,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_registration_with_invalid_city(self):
        data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "country": 1,
            "city": 2,
            "credit": "400",
        }

        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
