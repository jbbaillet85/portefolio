from django.test import TestCase
import pytest
from apps.project.models import Techno, Project
from django.contrib.auth import get_user_model

User = get_user_model()


class TestModelsProject(TestCase):
    def test_create_techno_valid_name(self):
        """Tests that a Techno object can be created with a valid name"""
        techno = Techno.objects.create(name="Python")
        assert techno.name == "Python"

    def test_create_techno_empty_name(self):
        """Tests that a Techno object cannot be created with an empty name"""
        with pytest.raises(ValueError):
            Techno.objects.create(name="")

    def test_create_techno_long_name(self):
        """Tests that a Techno object cannot be created with a name longer
          than 256 characters"""
        with pytest.raises(ValueError):
            Techno.objects.create(name="a" * 257)

    def test_create_project_with_all_fields(self):
        """Tests that a project can be created with all required fields"""
        user = User.objects.create(username='testuser')
        techno = Techno.objects.create(name='testtechno')
        project = Project.objects.create(name='testproject',
                                         description='testdescription',
                                         base_code='http://test.com',
                                         user=user)
        project.techno.add(techno)
        assert project.name == 'testproject'
        assert project.description == 'testdescription'
        assert project.base_code == 'http://test.com'
        assert project.user == user
        assert project.techno.first() == techno
