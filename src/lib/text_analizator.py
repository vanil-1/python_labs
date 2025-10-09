import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))) # добавляет путь к репозиторию с модулями
import text_token


def text_analizator(text):
    text_normalize = text_token.normalize(text)
    text_tokens = text_token.tokenize(text_normalize)
    text_freq = text_token.count_freq(text_tokens)
    text_top = text_token.top_n(dict(text_freq))

    len_max_word_top = max([len(word[0]) for word in text_top] + [7])
    len_max_freq_top = max([len(str(freq[1])) for freq in text_top] + [8])
    count_words_all = len(text_tokens)
    count_words_uniq = len(text_freq)

    print('Всего слов:', count_words_all)
    print('Уникальных слов:', count_words_uniq)
    print('Топ-5:')
    print('слова' + (' ' * (len_max_word_top - 5)) + '|' + ' частота')
    print(('-' * (len_max_word_top)) + '-' + ('-' * (len_max_freq_top)))
    for word_top_5 in text_top: print(f'{word_top_5[0]}: {word_top_5[1]}')