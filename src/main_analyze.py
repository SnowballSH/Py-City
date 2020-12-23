from src.scan import fetch, scanner
from src.visual import display


def analyze(url):
    _, path = fetch.clone(url)
    var = scanner.scan(path)
    return var
