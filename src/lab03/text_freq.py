import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))) # добавляет путь к репозиторию с модулями
import module_for_text.text_token as text_token


def text_analizator(text):
    text_normalize = text_token.normalize(text)
    text_tokens = text_token.tokenize(text_normalize)
    text_freq = text_token.count_freq(text_tokens)
    text_top = text_token.top_n(dict(text_freq))

    count_words_all = len(text_tokens)
    count_words_uniq = len(text_freq)
    
    print('Всего слов:', count_words_all)
    print('Уникальных слов:', count_words_uniq)
    print('Топ-5:')
    for word_top_5 in text_top: print(f'{word_top_5[0]}: {word_top_5[1]}')


text = sys.stdin.read()
text_analizator(text)