from main import dict_adder


def test_dict_adder_base() -> None:
    dict = {"first":2, "second":3}
    assert dict_adder(dict) == 5

def test_dict_adder_empty() -> None:
    dict = {}
    assert dict_adder(dict) == 0

def test_dict_adder_repeat() -> None:
    # repeats of keys dont get counted twice, last one is used
    dict = {"first":2, "first":5}
    assert dict_adder(dict) == 5

def test_dict_adder_noKey() -> None:
    dict = {"":1}
    assert dict_adder(dict) == 1

def test_dict_adder_noneValue() -> None:
    # dict_adder failed, overloaded with def dict_adder(dict, null_value=None):
    dict = {"first": None}
    assert dict_adder(dict) == 0

def test_dict_adder_noneValueAdded() -> None:
    dict = {"first": None, "second": 2}
    assert dict_adder(dict) == 2
