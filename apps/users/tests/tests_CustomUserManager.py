from django.test import TestCase
import pytest
from django.db import models
from apps.users.models import CustomUserManager


class TestCustomUserManager(TestCase):

    def test_create_user_with_email_and_password(self):
        """Tests that a user can be created with email and password"""
        email = "test@example.com"
        password = "password123"
        user = CustomUserManager().create_user(email=email, password=password)
        assert user.email == email
        assert user.check_password(password)

    def test_create_superuser_with_email_and_password(self):
        """Tests that a superuser can be created with email and password"""
        email = "admin@example.com"
        password = "admin123"
        superuser = CustomUserManager().create_superuser(email=email,
                                                         password=password)
        assert superuser.email == email
        assert superuser.check_password(password)
        assert superuser.is_staff
        assert superuser.is_superuser
        assert superuser.is_active

    def test_email_not_provided(self):
        """Tests that an error is raised when email is not provided"""
        with pytest.raises(ValueError):
            CustomUserManager().create_user(email=None, password="password123")

    def test_email_already_in_use(self):
        """Tests that an error is raised when email is already in use"""
        email = "test@example.com"
        password = "password123"
        CustomUserManager().create_user(email=email, password=password)
        with pytest.raises(models.IntegrityError):
            CustomUserManager().create_user(email=email, password=password)
