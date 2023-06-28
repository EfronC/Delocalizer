from cyfiles.modify_subs import modify_subs_py

subfile = "test.ass"
wordsfile = "tes.json"
name = modify_subs_py(subfile, wordsfile)
print(name)