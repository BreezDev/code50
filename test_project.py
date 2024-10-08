# Random Fortune Teller Project - Test File

import pytest
from project import get_fortune, provide_fortune, FORTUNES

def test_get_fortune():
    """Test that get_fortune returns a value from the FORTUNES list."""
    fortune = get_fortune()
    assert fortune in FORTUNES

def test_provide_fortune():
    """Test that provide_fortune returns a correctly formatted string."""
    name = "Alice"
    fortune = provide_fortune(name)
    assert fortune.startswith(f"{name}, ")
    assert fortune[0] != name  # Ensure the fortune is not just the name

def test_fortunes_not_empty():
    """Test that the FORTUNES list is not empty."""
    assert len(FORTUNES) > 0
