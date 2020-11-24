import os
import analyzer


def scan_path(path):
    return [f.path for f in os.scandir(path) if f.is_file()]


def scan_path_dict(path):
    return {f.path: '' for f in os.scandir(path) if f.is_dir()}


def scan_whole(path):
    filepaths = scan_path(path)
    dirpaths = scan_path_dict(path)
    return {"files": filepaths, "dirs": dirpaths}


def prim_scan(path):
    filepaths, dirpaths = scan_whole(path).values()
    for file in filepaths:
        with open(file, 'r') as f:
            code = f.read()
            yield (file, analyzer.analyze(code))
    for pa in dirpaths:
        yield {pa: tuple(prim_scan(pa))}


def scan(path):
    filepaths, dirpaths = scan_whole(path).values()
    for file in filepaths:
        with open(file, 'r') as f:
            code = f.read()
            yield {'root': (file, analyzer.analyze(code))}
    for pa in dirpaths:
        yield {pa: tuple(prim_scan(pa))}


if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint([*scan('sample')])
