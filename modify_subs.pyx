from modify_subs cimport modifySubs

def modify_subs_py(subfile: str):
    modifySubs(subfile.encode())

