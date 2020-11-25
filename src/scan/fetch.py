from git import Repo
import os


def clone(url):
    path = f'{os.getcwd()}\\src\\scan\\cache'
    name = url.split("/")[-1].split(".")[0]
    dirs = list(map(lambda x: x.path, filter(
        os.DirEntry.is_dir, os.scandir(path))))
    path += f'\\{name}'
    if path in dirs:
        repo = Repo(path)
    else:
        repo = Repo.clone_from(url, path)
    return repo, path


if __name__ == "__main__":
    clone("git://github.com/SnowballSH/Snow-lang.git")
