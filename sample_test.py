# sample_test.py
# 🧠 Basic sanity tests to verify GitHub Actions Python workflow setup

def test_addition():
    """Simple arithmetic test"""
    assert 2 + 2 == 4


def test_string_reverse():
    """String reversal check"""
    s = "voice"
    assert s[::-1] == "eciov"


def test_list_operations():
    """List manipulation check"""
    items = [1, 2, 3]
    items.append(4)
    assert sum(items) == 10


def test_dictionary_access():
    """Dictionary value retrieval"""
    data = {"repo": "man", "stars": 0}
    assert data.get("repo") == "man"
    assert "stars" in data


def test_boolean_logic():
    """Basic boolean validation"""
    condition = True
    assert condition is True
    assert not False
