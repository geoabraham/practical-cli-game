LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
NUMBERS = "1234567890"
SPACE_AND_SPECIAL_CHARATERS = " ¡!¿?.+*/@#$%&=()-_:;,ñÑáéíóúÁÉÍÓÚ"
SYMBOLS = LETTERS + NUMBERS + SPACE_AND_SPECIAL_CHARATERS


def main() -> None:
    """_summary_"""
    secret_message = "Mensaje súper secretooo!!! Iñaki."
    key = 13

    encrypted_message = encrypt_message(secret_message, key)
    assert encrypted_message != secret_message

    decrypted_message = encrypt_message(encrypted_message, key, mode=False)
    assert decrypted_message == secret_message


def encrypt_message(message: str, key: int, mode: bool = True) -> str:
    """
    Encrypts or decrypts a message using Caesar cipher.

    Args:
        message (str): The message to be encrypted/decrypted.
        key (int): The number of positions by which letters should be shifted.
        mode (bool, optional): If True, the function will encrypt the message.
            If False, it will decrypt the message. Defaults to True.

    Returns:
        str: The encrypted/decrypted message.
    """
    encrypted_message = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode:
                encrypted_index = (symbol_index + key) % len(SYMBOLS)
            else:
                encrypted_index = (symbol_index - key) % len(SYMBOLS)

            encrypted_message += SYMBOLS[encrypted_index]
        else:
            encrypted_message += symbol

    return encrypted_message


if __name__ == "__main__":
    main()
