import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib"))
)  # добавляет путь к репозиторию с модулями
import module_for_text.text_token as text_token


def text_analizator(text, n, tabl_state="0"):
    while tabl_state != "":
        tabl_state = input()
        text_normalize = text_token.normalize(text)
        text_tokens = text_token.tokenize(text_normalize)
        text_freq = text_token.count_freq(text_tokens)
        text_top = text_token.top_n(dict(text_freq), n)

        len_max_word_top = max([len(word[0]) for word in text_top] + [6])
        len_max_freq_top = max([len(str(freq[1])) for freq in text_top] + [8])
        count_words_all = len(text_tokens)
        count_words_uniq = len(text_freq)

        if tabl_state == "1":
            print("Всего слов:", count_words_all)
            print("Уникальных слов:", count_words_uniq)
            print(("-" * (len_max_word_top)) + "--" + ("-" * (len_max_freq_top)))
            print("слова" + (" " * (len_max_word_top - 4)) + "|" + " частота")
            print(("-" * (len_max_word_top)) + "--" + ("-" * (len_max_freq_top)))
            for word_top_5 in text_top:
                print(
                    f"{word_top_5[0]}{' ' * (len_max_word_top - len(word_top_5[0]) + 1)}| {word_top_5[1]}"
                )
        else:
            print("Всего слов:", count_words_all)
            print("Уникальных слов:", count_words_uniq)
            print(f"Топ-{n}:")
            for word_top_5 in text_top:
                print(f"{word_top_5[0]}: {word_top_5[1]}")
        print(("-" * (len_max_word_top)) + "--" + ("-" * (len_max_freq_top)))
