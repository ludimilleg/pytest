def eh_positivo(numero):
    return numero > 0

def test_eh_positivo():
    assert eh_positivo(5) is True
    assert eh_positivo(-5) is False