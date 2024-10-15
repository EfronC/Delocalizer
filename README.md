Delocalizer
===========

Delocalizer script to replace a set of words in a subtitle track on an MKV file for one specified on a JSON file.

## Installation
For Python:

[Source]
- Just create a Virtual Environment and run `pip install -r requirements`

[PYPI]
- `pip install delocalizer`

## Instructions

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

## Options
| Flag     | Description                                                                                             | Type   |
|----------|---------------------------------------------------------------------------------------------------------|--------|
| --shift  | Shift subtitles time for a desired amount of seconds.                                                   | float  |
| --j      | JSON file with the words to replace. REQUIRED.                                                          | string |
| --l      | Set which language to search for the subtitle track. ex: 'en'.                                          | string |
| --w      | Flag used to mark that a custom lambda can be used. Requires to have added the JSONLAMBDA in the .env . | string |
| --f      | Folder to output the generated MKVs. Subtitle files are kept in current folder if marked not to delete. | string |
| --k      | Flag used to keep the unlocalized subtitle file.                                                        | bool   |
| --no-mux | Flag used to skip the step to mux the subtitle file to the MKV.                                         | bool   |
