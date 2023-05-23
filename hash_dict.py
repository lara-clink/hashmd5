import time
import hashlib
import nltk

nltk.download('machado')
# Definir a senha alvo e seu hash MD5 correspondente
target_password = 'e8d95a51f3af4a3b134bf6bb680a213a'

# Carregar o dicionário de palavras em português da biblioteca nltk
nltk.download('rslp')
from nltk.corpus import machado
word_list = machado.words()

start_time = time.time()

for word in word_list:
    if len(word) == 5:
        hashed_word = hashlib.md5(word.encode()).hexdigest()
        if hashed_word == target_password:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Senha encontrada: {word}")
            print(f"Tempo decorrido: {elapsed_time:.2f} segundos")
            break
