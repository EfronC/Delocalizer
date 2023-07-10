Delocalizer
===========

Delocalizer script to replace a set of words in a subtitle track on an MKV file for one specified on a JSON file.

## Installation
For Python:

- Just create a Virtual Environment and run `pip install -r requirements`

For C modules(Optional):

- In progress...

## Instructions

- Make sure to create a .env file with the variable CYENV, which will tell the program if to use pure Python or Cython(If configured).
- Set the files you want to delocalize in the root folder.
- Create the JSON file, with this format
```
{
    "<word to search>":"new word",
    "<word to search>":"new word",
    ...
}
```

Recommendation, if a word is contained in another("Hello" and "Hello World"), set the lenghtier first.
- Once you have created those files, just execute the program with `python main.py --j <name json file>.json`