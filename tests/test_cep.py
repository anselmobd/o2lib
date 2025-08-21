from o2lib.validacao.cep import valido

def test_cep_valido():
    assert valido("12345678")
    assert valido("12345-678")
    assert valido("12.345-678")

def test_cep_invalido():
    assert not valido("1234")
    assert not valido("123456789")
    assert not valido("abcde123")
