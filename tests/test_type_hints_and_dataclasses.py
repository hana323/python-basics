"""Tests for the type hints and dataclasses example."""
import pytest

from python_concepts.examples.type_hints_and_dataclasses import (
    Person,
    create_person,
    get_person_info,
)


def test_person_creation() -> None:
    """Test basic Person creation."""
    person = Person(name="Alice", age=25)
    assert person.name == "Alice"
    assert person.age == 25
    assert person.email is None
    assert person.hobbies == []


def test_person_with_email() -> None:
    """Test Person creation with email."""
    person = Person(name="Bob", age=30, email="bob@example.com")
    assert person.email == "bob@example.com"


def test_person_add_hobby() -> None:
    """Test adding hobbies to a Person."""
    person = Person(name="Charlie", age=20)
    person.add_hobby("reading")
    person.add_hobby("gaming")
    assert person.hobbies == ["reading", "gaming"]


def test_person_is_adult() -> None:
    """Test the is_adult method."""
    adult = Person(name="Adult", age=18)
    minor = Person(name="Minor", age=17)
    assert adult.is_adult() is True
    assert minor.is_adult() is False


def test_create_person_function() -> None:
    """Test the create_person helper function."""
    person = create_person(name="Dave", age=35, email="dave@example.com")
    assert isinstance(person, Person)
    assert person.name == "Dave"
    assert person.age == 35
    assert person.email == "dave@example.com"


def test_get_person_info() -> None:
    """Test the get_person_info function."""
    adult = Person(name="Eve", age=25)
    minor = Person(name="Frank", age=15)

    assert get_person_info(adult) == "Eve is 25 years old (adult)"
    assert get_person_info(minor) == "Frank is 15 years old (minor)"
