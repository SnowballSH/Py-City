from . import analyzer
from dataclasses import dataclass
from typing import List
from randomcolor import *

from ursina import *


def grc():
    return map(int,
               RandomColor().generate(
                   luminosity=random.choice(("light", "bright")), format_="rgb", count=1
               )[0][4:-1].split(', '))


@dataclass
class FFile:
    """FFile: the File class
    """
    name: str
    stat: tuple

    def add_text(self, num=0, line=0, zdepth=0):
        fn = '/'.join(self.name.split('\\')[-2:])
        txt = f"""
.../{fn}
length: {self.stat[0]}
lines: {self.stat[1]}
variables: {self.stat[2]}
functions: {self.stat[3]}
""".strip().split('\n')

        txtlen = max(len(g) for g in txt)
        for i in range(len(txt)):
            txt[i] = txt[i].ljust(txtlen, ' ')

        bt = Button(
            model='cube',
            parent=scene,
            x=num / 0.8 - 2,
            y=line / 0.8 - 2,
            z=zdepth / 0.8 - 2,
            color=color.rgb(*grc()),
            scale=(0.6, 0.6, 0.6),
            tooltip=Tooltip(
                text=' '.join(txt),
                wordwrap=5),
            enabled=True)

        return bt


@dataclass
class FFolder:
    """FFile: the Folder class
    """
    name: str
    files: List[FFile]
    folders: list

    def add_text(self, display=True, depth=0, zdepth=0):
        fn = "Project: " + self.name.split('\\')[-1]
        x = Text(text=fn, origin=(-0.5 + len(fn) / 40, -5), scale=3) if display else None
        for i, u in enumerate(self.files):
            u.add_text(i, depth, zdepth)
        for i, u in enumerate(self.folders):
            u.add_text(False, depth + 1, i)
        return x


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
    return (f.path for f in os.scandir(path) if f.is_dir() and not f.path.endswith('.git'))


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
