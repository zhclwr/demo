def write_file(text, file_name="log.log", encoding="utf-8"):
    with open(file_name, mode='a', encoding=encoding) as f:
        f.write(text)


def read_file_text(file_name,  encoding="utf-8"):
    with open(file_name, mode='r', encoding=encoding) as f:
        return f.read()