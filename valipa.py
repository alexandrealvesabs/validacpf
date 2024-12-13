def is_valid_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
        return False

    # Validação dos dígitos verificadores
    def calculate_digit(cpf: str, factor: int) -> int:
        total = sum(int(digit) * (factor - index) for index, digit in enumerate(cpf[:factor - 1]))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    first_digit = calculate_digit(cpf, 10)
    second_digit = calculate_digit(cpf, 11)

    return cpf[-2:] == f"{first_digit}{second_digit}"
