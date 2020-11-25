from scan import fetch, scanner


def analyze(url):
    _, path = fetch.clone(url)
    return scanner.scan(path)


if __name__ == "__main__":
    print(analyze("https://github.com/SnowballSH/Snow-lang.git"))
