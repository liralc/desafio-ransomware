import os
import pyaes

# Nome do arquivo criptografado
encrypted_file_name = "teste.txt.ransomwaretroll"
decrypted_file_name = "teste.txt"

# Chave para descriptografia
key = b"testeransomwares"

try:
    # Verifica se o arquivo criptografado existe
    if not os.path.exists(encrypted_file_name):
        raise FileNotFoundError(f"Arquivo '{encrypted_file_name}' não encontrado.")

    with open(encrypted_file_name, "rb") as encrypted_file:
        file_data = encrypted_file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(file_data)

    with open(decrypted_file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    os.remove(encrypted_file_name)

    print(f"Arquivo '{encrypted_file_name}' foi descriptografado para '{decrypted_file_name}' e o original foi removido.")

except FileNotFoundError as e:
    print(f"Erro: {e}")
except PermissionError as e:
    print(f"Erro de permissão: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

