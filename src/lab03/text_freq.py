import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))) # добавляет путь к репозиторию с модулями
import text_token


def text_analuzator(text):
    text_normalize = text_token.normalize(text)
    text_tokens = text_token.tokenize(text_normalize)
    text_freq = text_token.count_freq(text_tokens)
    text_top = text_token.top_n(text_freq)

    count_words_all = len(text_tokens)
    count_words_uniq = len(text_freq)
    
    print('Всего слов:', count_words_all)
    print('Уникальных слов:', count_words_uniq)
    print('Топ-5:')
    print(text_top)
    for word_top_5 in text_top: print(word_top_5)
text = str(input())
print(text_analuzator(text))