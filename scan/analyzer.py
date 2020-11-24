import re


def analyze(code):
    """Analyze Code

    Args:
        code (string): Code

    Returns:
        tuple of:
            length of code,
            number of lines,
            amount of variables
    """

    code = code.strip()
    chunk = code
    var_count = 0
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
        res = re.match(r'(\w+\s*(:\s*\w+)?\s*=\s*.+)', chunk)
        if res:
            var_count += 1
            chunk = chunk[res.end():]
            continue

        chunk = chunk[1:]

    return len(code), len(code.split('\n')), var_count


if __name__ == "__main__":
    with open("sample/test.py") as f:
        print(analyze(f.read()))
