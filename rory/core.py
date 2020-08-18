# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['printnl', 'printdict', 'test_eqs']

# Cell
def printnl(*x,nl=2):
    """Print x separated by nl=2 newlines."""
    print(*x,sep='\n'*nl)

# Cell
def printdict(d,n=2):
    """Print n=2 pairs from a dict."""
    l = list(d.items())[:n]
    for k,v in l:
        print(f'Key ({type(k).__name__}): "{k}"\nValue ({type(v).__name__}): {v}\n')

# Cell
def test_eqs(*o):
    """recursive test_eq"""
    l=[*o]
    if len(l) == 2:
        return test_eq(l[0], l[1])
    else:
        return test_eqs(*l[1:])