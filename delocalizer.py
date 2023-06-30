import pysubs2
import argparse
import json
import glob
import os

from cyfiles.modify_subs import modify_subs_py
from merger import Merger

class Delocalizer:

    def __init__(self):
        self.LANGUAGES = ["eng", "spa"]
        self.ERRORS = []
        self.language = "eng"
        self.wordsfile = None
        self.file = None
        self.subfile = None
        self.merger = Merger()

    def modify_subs(self, jname):
        try:
            f = open(jname, encoding="utf-8")
            new_lines = json.load(f)
            nfilename = "[Delocalized] "+self.subfile

            subs = pysubs2.load(self.subfile, encoding="utf-8")
            for nl, line in enumerate(subs):
                if line.type == "Dialogue":
                    line.text = new_lines[str(nl+1)]
            subs.save(nfilename)
            return nfilename
        except Exception as e:
            print(e)
            return False

    def replace_words(self, f):
        try:
            name = modify_subs_py(str(f), str(self.wordsfile))
            if name != "":
                return name
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def shift_subs(self, delta):
        try:
            subs1 = pysubs2.load(self.file, encoding="utf-8")
            subs1.shift(s=delta)
            msub = "m_" + self.file
            subs1.save(msub)

            return msub
        except Exception as e:
            print(e)
            return False

    def prepare_data(self, args):
        try:
            if args.jfile:
                self.wordsfile = args.jfile
            else:
                raise Exception("No JSON file indicated")
            if args.language:
                if args.language in LANGUAGES:
                    self.language = args.language

            return True
        except Exception as e:
            print(e)
            return False

    def print_errors(self):
        try:
            if len(ERRORS) > 0:
                print("There were errors:")
                for i in ERRORS:
                    print("-", i)
            else:
                print("No errors")
        except Exception as e:
            print(e)

    def get_index(self):
        try:
            streams = self.merger.get_streams(self.file)
            index = self.merger.get_language_index(self.language)

            return index
        except Exception as e:
            print(e)
            return -1

    def generate_params(self):
        try:
            sfiles = self.merger.get_number_subs()
            filename = os.path.splitext(self.file)[0]
            newfilename = "."+os.sep+"Finished"+os.sep+filename + '.mkv'

            ads = ["-metadata:s:s:{}".format(sfiles), "language=eng", "-metadata:s:s:{}".format(sfiles), "handler_name=English", "-metadata:s:s:{}".format(sfiles), "title=Unlocalized", "-max_interleave_delta", "0", "-disposition:s:0", "0", "-disposition:s:{}".format(sfiles), "default", newfilename]
            return ads
        except Exception as e:
            print(e)
            return []

    def delocalize(self):
        try:
            files = glob.glob('*.mkv')
            index = -1
            for f in files:
                print("Extracting: ", f)
                self.file = f
                self.merger.set_file(f)
                index = self.get_index()

                if index > -1:
                    print("Subtitles found at", index)
                    self.subfile = self.merger.demux(self.file, index, "subfile.ass")
                    if self.subfile:
                        print("Delocalizing...")
                        word_json = self.replace_words(self.subfile)
                        unloc_sub = self.modify_subs(word_json)
                        if unloc_sub:
                            os.remove(self.subfile)
                            os.remove(word_json)
                            print("Muxxing with file:", unloc_sub)
                            params = self.generate_params()
                            r = self.merger.mux(f, unloc_sub, params)
                            if r:
                                os.remove(unloc_sub)
                            else:
                                print("Failed to mux sub!")
                                self.ERRORS.append(str(self.file))
                        else:
                            print("Failed to modify subs!")
                            self.ERRORS.append(str(self.file))
                    else:
                        print("Failed to extract Subtitle!")
                        self.ERRORS.append(str(self.file))
                else:
                    print("Subtitles not found!")
                    self.ERRORS.append(str(self.file))
        except Exception as e:
            print(e)
            return False