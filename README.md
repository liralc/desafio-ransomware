# Projeto de Criptografia de Arquivos com AES

Este é um projeto simples de criptografia de arquivos utilizando o algoritmo AES em modo CTR (Counter). O código realiza a criptografia de um arquivo de texto e salva o arquivo criptografado com um sufixo específico.

## Funcionalidade

- **Criptografar Arquivo**: O programa lê um arquivo de texto, criptografa seu conteúdo usando a chave definida e salva o arquivo criptografado.
- **Remover Arquivo Original**: Após criptografar, o arquivo original é removido do sistema.
- **Armazenar Arquivo Criptografado**: O arquivo criptografado é salvo com o sufixo `.ransomwaretroll`.

## Requisitos

Antes de executar o código, verifique se o seguinte está instalado no seu ambiente:

- **Python 3.x**: Certifique-se de que o Python esteja instalado.
- **pyaes**: Biblioteca para criptografia AES. Você pode instalar com o seguinte comando:
  
  ```bash
  pip install pyaes
  ```

## Como Usar

### 1. Preparar o Arquivo

Certifique-se de que o arquivo que você deseja criptografar esteja presente no mesmo diretório do script. O arquivo deve ser um arquivo de texto (por exemplo, `teste.txt`).

### 2. Executar o Script

Execute o script Python. O código criptografará o arquivo e o salvará com o sufixo `.ransomwaretroll`.

```bash
python criptografar.py
```

### 3. Arquivo Criptografado

Após a execução do script, o arquivo original será removido e um novo arquivo criptografado será gerado no mesmo diretório. O nome do arquivo criptografado será o nome do arquivo original com o sufixo `.ransomwaretroll`. Por exemplo, se o arquivo original for `teste.txt`, o arquivo criptografado será `teste.txt.ransomwaretroll`.

### 4. Descriptografar o Arquivo (Opcional)

Se desejar descriptografar o arquivo, você pode criar um script de descriptografia utilizando a chave correta e o modo AES CTR.

## Estrutura de Arquivos

O projeto contém os seguintes arquivos:

- `criptografar.py`: Script Python para criptografar o arquivo.
- `README.md`: Documento de instrução (este arquivo).

## Como Funciona

1. O arquivo original é lido no modo binário (`rb`).
2. Os dados do arquivo são criptografados usando o algoritmo AES no modo CTR, com uma chave definida (`testeransomwares`).
3. O arquivo criptografado é salvo com o sufixo `.ransomwaretroll`.
4. O arquivo original é removido para garantir que ele não seja acessado após a criptografia.

## Segurança

A chave de criptografia utilizada no exemplo é uma chave estática definida no código (`testeransomwares`). Em um ambiente de produção, recomenda-se gerar uma chave aleatória e mantê-la segura.

