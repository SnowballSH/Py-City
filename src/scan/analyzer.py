import re


def analyze(code):
    """Analyze Code

    Args:
        code (string): Code

    Returns:
        tuple of:
            length of code,
            number of lines,
            amount of variables,
            amount of functions
    """

    code = code.strip()
    chunk = code
    var_count = 0
    func_count = 0
    class_count = 0
    while chunk:
        # string
        res = re.match(r"('''(\\'|[^'])*''')", chunk)
        if res:
            chunk = chunk[res.end():]
            continue

        res = re.match(r'("""(\\"|[^"])*""")', chunk)
        if res:
            chunk = chunk[res.end():]
            continue

        res = re.match(r'("(\\"|[^\n\r"])*")', chunk)
        if res:
            chunk = chunk[res.end():]
            continue

        res = re.match(r"('(\\'|[^\n\r'])*')", chunk)
        if res:
            chunk = chunk[res.end():]
            continue

        # int
        res = re.match(r'(\d+)', chunk)
        if res:
            chunk = chunk[res.end():]
            continue

        # variable
        res = re.match(r'((\w+\s*\.\s*)*\w+\s*(:\s*\w+)?\s*=\s*.+)', chunk)
        if res:
            var_count += 1
            chunk = chunk[res.end():]
            continue

        # function
        res = re.match(r'(def\s*\w+\s*\([^\n\r]*\)\s*:)', chunk)
        if res:
            func_count += 1
            chunk = chunk[res.end():]
            continue

        # class
        res = re.match(r'(class\s*\w+(\s*\([^\n\r]*\))?\s*:)', chunk)
        if res:
            class_count += 1
            chunk = chunk[res.end():]
            continue

        chunk = chunk[1:]

    return len(code), len(code.split('\n')), var_count, func_count, class_count


if __name__ == "__main__":
    with open("sample/test.py") as f:
        print(analyze(f.read()))
