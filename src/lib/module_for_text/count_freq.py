def count_freq(tokens: list[str]):
    token_keys_all = sorted(set(tokens))
    return sorted({token_key: tokens.count(token_key) for token_key in token_keys_all}.items(), key = lambda item: (-item[1], item[0]))