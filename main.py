from src.main_analyze import analyze, display

if __name__ == "__main__":
    data = analyze("https://github.com/Tech-With-Tim/twtcodejam.net")
    display(data)
