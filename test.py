import pytest


@pytest.mark.parametrize("test_input, expected", [(8, 108), (6, 106), (42, 142)])
def test_sum(test_input, expected):
    n = 100
    assert n + test_input == expected


def test_decrease():
    a = 10
    b = 20
    assert b - a == 10


def testAddElementInDict():
    dictionary = {'dict1': 1, 'dict2': 2}
    dictionary.update({'dict3': 3})
    assert dictionary == {'dict1': 1, 'dict2': 2, 'dict3': 3}


def testCheckRemovingNonexistElement():
    dictionary1 = {'dict1': 1, 'dict2': 2, 'dict3': 3}
    with pytest.raises(KeyError):
        assert dictionary1.pop('ss')


def testAddElementInSet():
    a = set('hello')
    a.add('w')
    assert a == set('hellow')


def testRemoveElementInSet():
    a = set('hellow')
    a.remove('w')
    assert a == set('hello')
