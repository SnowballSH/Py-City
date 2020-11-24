import os
import analyzer
from dataclasses import dataclass


@dataclass
class FFile:
    name: str
    stat: tuple


@dataclass
class FFolder:
    name: str
    files: any
    folders: any


def scan_path(path):
    return (f.path for f in os.scandir(path) if f.is_file())


def scan_path_dict(path):
    return (f.path for f in os.scandir(path) if f.is_dir())


def scan_whole(path):
    filepaths = scan_path(path)
    dirpaths = scan_path_dict(path)
    return filepaths, dirpaths


def scan(path):
    filepaths, dirpaths = scan_whole(path)
    l = []
    for file in filepaths:
        with open(file, 'r') as f:
            code = f.read()
            l.append(FFile(file, analyzer.analyze(code)))
    j = []
    for pa in dirpaths:
        j.append(scan(pa))
    return FFolder(path, l, j)


if __name__ == "__main__":
    res = scan('sample')
    import pprint
    pp = pprint.PrettyPrinter(indent=4)

    pp.pprint(vars(res))
