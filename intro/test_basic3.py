from .funcoes import email_valido
from .funcoes import dividir

def test_email_valido():
    assert email_valido("ex@dominio.com") is True
    assert email_valido("exemplo.com") is False

def test_dividir():
    assert dividir(4, 2) == 2
    assert dividir(4, 0) is None
