import crypt
import time

password = {
    "1": {
        "salt": "$y$j9T$nFwHNF0c3SCbH6ESyzSKw.",
        "senha": "$y$j9T$nFwHNF0c3SCbH6ESyzSKw.$ph1Q6UMJnIyAU6O7ZLYH14H5C4.V1SJjcrjLqVQuG00",
        "arquivo": "br-utf8.txt",
        "usuario": "Pimpolho"
    },
    "2": {
        "salt": "$y$j9T$5LImmws2fco9AeRmLSB2j0$",
        "senha": "$y$j9T$5LImmws2fco9AeRmLSB2j0$fYPmdqu1Q/FDiwPJgkCIW9wX76w12SNEiYAodUzafo5",
        "arquivo": "rockyou.txt",
        "usuario": "testeadm"
    }
}

for info in password.items():
    file_name = str(info[1]["arquivo"])
    senha = str(info[1]["senha"])
    salt = str(info[1]["salt"])
    usuario = str(info[1]["usuario"])
    
    start_time = time.time()

    with open(file_name, "r", encoding="utf-8", errors="replace") as dicionario:
        for linha in dicionario:

            # Para desconsiderar a quebra de linha no final de cada palavra
            palavra = linha.replace("\n", "")

            # Criptografar a senha usando o salt
            senha_criptografada = crypt.crypt(palavra, salt)

            if senha_criptografada == senha:
                print("+-----------------------+")
                print("|    Usuário: %s  |" %(usuario))
                print("|      Senha: %s  |" % (palavra))
                print("|  Tempo para decifrar: |")
                print("|       %s segundos   |" % (str(round((time.time() - start_time),2))))
                print("+-----------------------+")
                print()
                break
