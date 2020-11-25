from scan import fetch, scanner


def analyze(url):
    _, path = fetch.clone(url)
    var = scanner.scan(path)
    return var


if __name__ == "__main__":
    print(analyze("https://github.com/SnowballSH/BFCT.git"))
