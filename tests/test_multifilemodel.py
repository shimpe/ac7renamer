"""Tests for MultiFileModel.sanitize_filename behavior."""
import pytest


@pytest.fixture
def model(qapp):
    from ac7renamer.multifilemodel import MultiFileModel

    return MultiFileModel(0, 6, parent=None)


def test_appends_ac7_when_missing(model):
    assert model.sanitize_filename("MyStyle") == "MyStyle.AC7"


def test_preserves_uppercase_ac7(model):
    assert model.sanitize_filename("MyStyle.AC7") == "MyStyle.AC7"


def test_preserves_lowercase_ac7(model):
    # The endswith check is case-insensitive, so .ac7 is left alone.
    assert model.sanitize_filename("mystyle.ac7") == "mystyle.ac7"


def test_replaces_spaces_with_underscores(model):
    assert model.sanitize_filename("my style") == "my_style.AC7"


def test_strips_surrounding_whitespace(model):
    assert model.sanitize_filename("   trimmed   ") == "trimmed.AC7"


def test_strips_unsafe_characters(model):
    assert model.sanitize_filename("a!b@c#d") == "abcd.AC7"


def test_keeps_dot_and_hyphen_and_underscore(model):
    assert model.sanitize_filename("a-b_c.d") == "a-b_c.d.AC7"


def test_empty_input_returns_empty(model):
    # No characters means no .AC7 is appended.
    assert model.sanitize_filename("") == ""


def test_only_unsafe_chars_returns_empty(model):
    # After sanitization the result is empty; nothing gets the .AC7 suffix.
    assert model.sanitize_filename("!@#$%") == ""
