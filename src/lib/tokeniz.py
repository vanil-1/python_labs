import re

def tokeniz(text: str): return re.findall( r'\w+(?:-\w+)*', text)