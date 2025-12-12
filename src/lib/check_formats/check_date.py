from datetime import datetime


def check_date(
    date: str,
    formats_date=["%Y/%m/%d", "%Y.%m.%d", "%d/%m/%Y", "%d.%m.%Y"],
    format_true=0,
) -> bool:
    for format in formats_date:
        try:
            datetime.strptime(date, format)
            format_true = format
            break
        except:
            pass
    if format_true != 0:
        return datetime.strptime(date, format_true)
    else:
        raise ValueError(
            "WARNING: birthdate format might be invalid, you should use format: "
            f"yyyy/mm/dd | yyyy.mm.dd | dd/mm/yyyy | dd.mm.yyyy; also type of birthdate is str: {date}"
        )
