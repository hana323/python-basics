"""Example demonstrating Python type hints and dataclasses.

This module shows how to use type hints and dataclasses to create
type-safe and clean data structures.
"""
from dataclasses import dataclass


@dataclass
class Person:
    """A simple person data class with type hints."""
    name: str
    age: int
    email: str | None = None
    hobbies: list[str] = None

    def __post_init__(self) -> None:
        """Initialize default values after dataclass initialization."""
        if self.hobbies is None:
            self.hobbies = []

    def add_hobby(self, hobby: str) -> None:
        """Add a new hobby to the person's list of hobbies."""
        self.hobbies.append(hobby)

    def is_adult(self) -> bool:
        """Check if the person is an adult (18 or older)."""
        return self.age >= 18


def create_person(name: str, age: int, email: str | None = None) -> Person:
    """Create a new Person instance with the given parameters."""
    return Person(name=name, age=age, email=email)


def get_person_info(person: Person) -> str:
    """Get a formatted string with person's information."""
    adult_status = "adult" if person.is_adult() else "minor"
    return f"{person.name} is {person.age} years old ({adult_status})" 