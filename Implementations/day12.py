from typing import List
    
def part1(lines: List[str]):
    edges = {"start": [], "end": []}
    for line in lines:
        s, e = line.split("-")
        if s not in edges:
            edges[s] = []
        if e not in edges:
            edges[e] = []
        edges[s].append(e)
        edges[e].append(s)

    paths = []
    def get_paths(p):
        new_paths = []
        for _p in p:
            last = _p[-1] 
            for n in edges[last]:
                if (n in _p and n.isupper()) or n not in _p:
                    np = _p + [n]
                    new_paths.append(np)

        return new_paths

    def completed_path(p):
        if p[-1] == "end":
            paths.append(p)
            return True
        return False

    _paths = [["start"]]
    while len(_paths) > 0:
        _paths = get_paths(_paths)
        _paths = [x for x in _paths if not completed_path(x)]

    return len(paths)

def part2(lines: List[str]):
    edges = {"start": [], "end": []}
    for line in lines:
        s, e = line.split("-")
        if s not in edges:
            edges[s] = []
        if e not in edges:
            edges[e] = []
        edges[s].append(e)
        edges[e].append(s)

    paths = []
    def get_paths(p):
        def check_allowed_twice(c, __p):
            if n == "start":
                return False

            if c in __p:
                for _c in set(__p):
                    if _c.islower() and __p.count(_c) > 1:
                        return False
            return True

        new_paths = []
        for _p in p:
            last = _p[-1] 

            for n in edges[last]:
                if (n in _p and n.isupper()) or n not in _p:
                    np = _p + [n]
                    new_paths.append(np)
                elif check_allowed_twice(n, _p):
                    np = _p + [n]
                    new_paths.append(np)
        return new_paths

    def completed_path(p):
        if p[-1] == "end":
            paths.append(p)
            return True
        return False

    _paths = [["start"]]
    while len(_paths) > 0:
        _paths = get_paths(_paths)
        _paths = [x for x in _paths if not completed_path(x)]

    return len(paths)