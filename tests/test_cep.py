from o2lib.validacao.cep import validar

def test_cep_valido():
    assert validar("12345678")
    assert validar("12345-678")
    assert validar("12.345-678")

def test_cep_invalido():
    assert not validar("1234")
    assert not validar("123456789")
    assert not validar("abcde123")
