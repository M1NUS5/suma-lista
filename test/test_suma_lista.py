import pytest
from suma_lista import suma_lista


def test_suma_correcta():
    assert suma_lista([1, 2, 3, 4]) == 10


def test_lista_un_elemento():
    assert suma_lista([5]) == 5


def test_lista_vacia():
    with pytest.raises(ValueError):
        suma_lista([])


def test_elemento_no_numerico():
    with pytest.raises(TypeError):
        suma_lista([1, 2, "3"])


def test_no_es_lista():
    with pytest.raises(TypeError):
        suma_lista("123")