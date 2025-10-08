def count_freq(tokens: list[str]):
    token_keys_all = sorted(set(tokens))
    return {token_key: tokens.count(token_key) for token_key in token_keys_all}