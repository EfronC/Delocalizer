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

