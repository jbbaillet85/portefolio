from django.test import TestCase
import pytest
from apps.users.models import Skill


class TestsSkills(TestCase):

    def test_create_skill_with_valid_name(self):
        """Tests that a Skill object can be created with a valid name"""
        skill = Skill.objects.create(name="Python")
        assert skill.name == "Python"

    def test_retrieve_name_of_skill(self):
        """Tests that the name of a Skill object can be retrieved"""
        skill = Skill.objects.create(name="Java")
        assert str(skill) == "java"

    def test_create_skill_with_empty_name(self):
        """Tests that a Skill object cannot be created with an empty name"""
        with pytest.raises(Exception):
            Skill.objects.create(name="")

    def test_create_skill_with_name_longer_than_100_characters(self):
        """Tests that a Skill object cannot be created with
        a name longer than 100 characters"""
        with pytest.raises(Exception):
            Skill.objects.create(name="a" * 101)
