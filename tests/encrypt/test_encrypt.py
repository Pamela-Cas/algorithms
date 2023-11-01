import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("meleca", "2")
    assert encrypt_message("meleca", 0) == "acelem"
    assert encrypt_message("meleca", 1) == "m_acele"
    assert encrypt_message("meleca", 2) == "acel_em"
    assert encrypt_message("meleca", 10) == "acelem"
    assert encrypt_message("", 2) == ""

