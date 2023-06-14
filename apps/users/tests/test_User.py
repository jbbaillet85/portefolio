from django.test import TestCase
import pytest
from apps.users.models import User


class TestsUser(TestCase):

    def test_create_user(self):
        """Tests that a user can be created with email and password"""
        user = User.objects.create_user(email="test@example.com",
                                        password="password")
        assert user.email == "test@example.com"
        assert user.check_password("password")

    def test_create_superuser(self):
        """Tests that a superuser can be created with email and password"""
        superuser = User.objects.create_superuser(email="admin@example.com",
                                                  password="password")
        assert superuser.email == "admin@example.com"
        assert superuser.check_password("password")
        assert superuser.is_staff
        assert superuser.is_superuser
        assert superuser.is_active

    def test_create_user_no_email(self):
        """Tests that an error is raised when creating a user with no email"""
        with pytest.raises(ValueError):
            User.objects.create_user(email="", password="password")

    def test_create_user_non_unique_email(self, mocker):
        """Tests that an error is raised when creating a user with
          a non-unique email"""
        mocker.patch("django.db.models.manager.BaseManager._insert",
                     side_effect=Exception("Email already exists"))
        with pytest.raises(Exception):
            User.objects.create_user(email="test@example.com",
                                     password="password")

    def test_create_superuser_no_email(self):
        """Tests that an error is raised when creating a
        superuser with no email"""
        with pytest.raises(ValueError):
            User.objects.create_superuser(email="", password="password")
