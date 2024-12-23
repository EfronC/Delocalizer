Delocalizer
===========

Delocalizer script to replace a set of words in a subtitle track on an MKV file for one specified on a JSON file. You can find example resources [here](https://efronc.github.io/delocalizer-files).

## Installation
For Python:

[Source]
- Install Poetry
- Run `poetry install`
- Execute the commands through `poetry run <command> <args>`

or

- Create a Virtual Environment and run `pip install -r requirements`
- Execute the files directly, example `python delocalizer/main.py <args>`

[PYPI]
- `pip install delocalizer`

## Delocalizer

Replace a set of words, defined through a JSON file, a remux the new subtitle file.

### Instructions

- [Optional] Create a .env file with the variable CYENV, which will tell the program if to use pure Python or Cython, default if not defined is Cython.
- Set the files you want to delocalize in the folder.
- Create the JSON file, with this format
```
{
    "<word to search>":"new word",
    "<word to search>":"new word",
    ...
}
```

Recommendation: If a word is contained in another("Hello" and "Hello World"), set the lengthier first.
- Once you have created those files, just execute the program with `delocalizer --j <name json file>.json`

### Options
| Flag     | Description                                                                                             | Type   | Required |
|----------|---------------------------------------------------------------------------------------------------------|--------|----------|
| --j      | JSON file with the words to replace. REQUIRED.                                                          | string |     ✓    |
| --l      | Set which language to search for the subtitle track. ex: 'eng'.                                         | string |     ✗    |
| --i      | Index of the subtitle track.                                                                            | int    |     ✗    |
| --shift  | Shift subtitles time for a desired amount of seconds.                                                   | float  |     ✗    |
| --w      | Flag used to mark that a custom lambda can be used. Requires to have added the JSONLAMBDA in the .env . | bool   |     ✗    |
| --f      | Folder to output the generated MKVs. Subtitle files are kept in current folder if marked not to delete. | string |     ✗    |
| --k      | Flag used to keep the unlocalized subtitle file.                                                        | bool   |     ✗    |
| --no-mux | Flag used to skip the step to mux the subtitle file to the MKV.                                         | bool   |     ✗    |

## Examples

- Delocalize all files on current folder.
```
delocalizer --j sample.json
```


## Extractor

Allows to extract one or all subtitle tracks, and also to append new tracks to an MKV file.

### Instructions

- Add your file or files into the folder.
- Execute the command

### Options
| Flag  | Description                        | Type   | Required |
|-------|------------------------------------|--------|----------|
| --mux | Whether mux or demux               | bool   | ✓        |
| --m   | If multiple files will be affected | bool   | ✗        |
| --f   | Folder to save                     | string | ✗        |
| --s   | Subtitle file to append            | string | if mux   |
| --i   | Input MKV filename                 | string | if mux   |
| --idx | Index of the subtitle to extract   | int    | ✗        |
| --p   | Print language indexes             | bool   | ✗        |

### Examples

- Extract one subtitle
```
extractor --no-mux --idx 2 --i 'file.mkv'
```

- Extract all subtitles from one file
```
extractor --no-mux --i 'file.mkv'
```

- Extract from all files
```
extractor --no-mux --m
```

- Mux subtitle
```
extractor --mux --i 'file.mkv' --s 'file.ass'
```

- Print subtitle tracks
```
extractor --p --m
```


## Honorifics

Allows to use a reference subtitle file to add honorifics to an english subtitle file. It also allows to pass another file with a translation using honorifics on a non-japanese language, so it will add the honorifics, if possible, to the english one, currently only tested on Esp-Eng.

### Instructions

- Add the english and japanese subtitle files in your current folder.
- Add a names JSON file with the next format. Make sure that for the JP name it uses either japanese or roman characters, depending on how it is in the reference file.
```
{
    "<english name>": "<japanese name>"
}
```
- Add an honorifics.json file to your current folder. A sample of this file can be fetched with
```
from subdeloc_tools.subtools import SubTools
import json

json.dumps(SubTools.get_default_honorifics_file())
```
- Call the command to generate the new subtitle file

### Options
| Flag     | Description                     | Type   | Required |
|----------|---------------------------------|--------|----------|
| --f      | Folder to save                  | string | ✗        |
| --ref    | Reference subtitle              | string | ✓        |
| --i      | Original subtitle               | string | ✓        |
| --n      | Names file                      | string | ✓        |
| --tokens | If not using japanese reference | bool   | ✗        |
| --honor  | Custom path for honorifics file | string | ✗        |
| --o      | Custom output name for result   | string | ✗        |

### Examples

- Fix honorifics
```
honorifics --ref 'jap.ass' --i 'eng.ass' --n 'names.json' --honor './honorifics.json'
```

- Fix from tokens
```
honorifics --ref 'ref.ass' --i 'orig.ass' --n 'names.json' --honor './honorifics.json' --tokens
```

Sister projects:
- [SubDelocalizer Tools](https://github.com/EfronC/subdeloc_tools)
- [C Helpers](https://github.com/EfronC/subdeloc_helper)