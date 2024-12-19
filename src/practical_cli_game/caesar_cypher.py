LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
NUMBERS = "1234567890"
SPACE_AND_SPECIAL_CHARATERS = " ¡!¿?.+*/@#$%&=()-_:;,ñÑáéíóúÁÉÍÓÚ"
SYMBOLS = LETTERS + NUMBERS + SPACE_AND_SPECIAL_CHARATERS


def main() -> None:
    """_summary_"""
    secret_message = "Mensaje súper secretooo!!! Iñaki."
    key = 13

    encrypted_message = encrypt_message(secret_message, key)

    print(encrypted_message)

    decrypted_message = encrypt_message(encrypted_message, key, "decrypt")

    print(decrypted_message)


def encrypt_message(message: str, key: int, mode: str = "encrypt") -> str:
    """_summary_

    Args:
        message (str): _description_
        key (int): _description_
        mode (str, optional): _description_. Defaults to "encrypt".

    Returns:
        _type_: _description_
    """
    encrypted_message = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode == "encrypt":
                encrypted_index = symbol_index + key
            elif mode == "decrypt":
                encrypted_index = symbol_index - key

            # Handle wrap-around, if needed:
            if encrypted_index >= len(SYMBOLS):
                encrypted_index -= len(SYMBOLS)
            elif encrypted_index < 0:
                encrypted_index += len(SYMBOLS)

            encrypted_message += SYMBOLS[encrypted_index]
        else:
            encrypted_message += symbol

    return encrypted_message


if __name__ == "__main__":
    main()
