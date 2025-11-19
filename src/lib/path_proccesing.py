from pathlib import Path

def path_proccesing(path_str: str, out: bool):
    path = Path(path_str)
    if out: path.parent.mkdir(parents = True, exist_ok = True)
    return path

def path_is_json(path: Path, error = None):
    if path.exists():
        if path.suffix.lower() == ".json": error = False
        else: error = ValueError
    else: error = FileNotFoundError
    return error

def path_is_csv(path: Path, error = None):
    if path.exists():
        if path.suffix.lower() == ".csv": error = False
        else: error = ValueError
    else: error = FileNotFoundError
    return error