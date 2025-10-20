import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Dawid12345#", True),

        ("Daw@1", False),  # to short
        ("password@1", False),  # brak duzych liter, brak cyfry, brak znaku specjalnego
        ("A" * 17 + "1@", False),  # za dlugie
        ("Password1", False),
        ("Password#", False),
        ("Pass word#", False),
    ],
)
def test_check_password(password, expected):
    result = check_password(password)
    assert result == expected
