from pathlib import Path


def inicialPath(path: str, path_suffix: tuple | list | str):
    path = Path(path)
    if path.suffix.lower() in path_suffix:
        if not path.exists():
            path.write_text("", encoding="utf-8")
        return path
    else:
        raise ValueError(f"Your file must be {path_suffix}!")


def pathProccesing(path: str, path_out: bool, path_suffix: tuple | list | str):
    path = Path(path)
    if path.suffix.lower() in path_suffix:
        if path.exists():
            return path
        elif not (path.exists()) and path_out:
            path.parent.mkdir(parents=True, exist_ok=True)
            return path
        else:
            return FileNotFoundError
    else:
        return ValueError(f"Your file must be {path_suffix}!")
