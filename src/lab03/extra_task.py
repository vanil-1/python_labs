import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))) # добавляет путь к репозиторию с модулями
import module_for_text.text_analizator as text_analizator

text = sys.stdin.read()
text_analizator.text_analizator(text)