import os
from . import analyzer
from dataclasses import dataclass


@dataclass
class FFile:
    """FFile: the File class
    """
    name: str
    stat: tuple


@dataclass
class FFolder:
    """FFile: the Folder class
    """
    name: str
    files: any
    folders: any


def scan_path(path):
    """Scan all files

    Args:
        path (str): path

    Returns:
        generator: Tuple of all file path
    """
    return (f.path for f in os.scandir(path) if f.is_file() and
            any((f.path.endswith('.py'), f.path.endswith(
                '.pyx', f.path.endswith('.pyc')))))


def scan_dir(path):
    """Scan all directories

    Args:
        path (str): path

    Returns:
        generator: Tuple of all folder path
    """
    return (f.path for f in os.scandir(path) if f.is_dir())


def scan_whole(path):
    """Scan the whole directory

    Args:
        path (str): path

    Returns:
        tuple: filepaths and dirpaths
    """
    filepaths = scan_path(path)
    dirpaths = scan_dir(path)
    return filepaths, dirpaths


def scan(path):
    """Main scan function

    Args:
        path (str): the path of folder

    Returns:
        FFolder: FFolder object of the folder,
        containing all analyzed information
    """
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
