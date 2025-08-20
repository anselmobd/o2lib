import re


def validar(valor: str) -> bool:
    """
    Valida se o valor representa um CEP brasileiro válido.
    Formatos aceitos:
    - 99999999
    - 99999-999
    - 99.999-999
    """
    if not isinstance(valor, str):
        return False

    padrao = re.compile(r"^\d{8}$|^\d{5}-\d{3}$|^\d{2}\.\d{3}-\d{3}$")
    return bool(padrao.match(valor))

