# AUTOGENERATED! DO NOT EDIT! File to edit: helpers.ipynb (unless otherwise specified).

__all__ = ['pnl', 'printdict', 'test_eqs', 'flatten']

# Cell
def pnl(*x,nl=1):
    """Print x separated by nl newlines."""
    print(*x,sep='\n'*nl)
def printdict(d,n=3):
    """Print n=2 pairs from a dict."""
    l = list(d.items())[:n]
    for k,v in l:
        print(f"{k} ({type(k).__name__}): {v} ({type(v).__name__})")

# Cell
def test_eqs(*o):
    """recursive test_eq"""
    l=[*o]
    if len(l) == 1: raise TypeError("test_eqs recieved only 1 arg.")
    if len(l) == 2: return test_eq(l[0], l[1])
    else:           return test_eqs(*l[1:])

# Cell
def flatten(l):
    def _recur(l,res):
        for o in l:
            if   isinstance(o,list): _recur(o,res)
            elif isinstance(o,L)   : _recur(o,res)
            else: res.append(o)
        return res
    return _recur(l, L())