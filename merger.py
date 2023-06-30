import subprocess
import sys
import json
import os


class Merger:

    TASKS = {"demux":1, "mux":2}
    STATUSES = {"NOFILE":0, "INITIALIZED":1, "MUXXING": 2, "DEMUXXING":3}

    def __init__(self):
        self.status = 0
        self.finished = "./Finished"
        self.streams = None
        self.file = None

    def get_streams(self, fname):
        try:
            if self.status == self.STATUSES["INITIALIZED"]:
                return self.streams
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def mux(self, f, subtitle, params):
        try:
            if self.status == self.STATUSES["INITIALIZED"] and os.path.isfile(subtitle):
                args = ["ffmpeg", "-loglevel", "quiet", "-y", "-i", f, "-i", subtitle, "-c", "copy", "-map", "0", "-map", "1"] + params
                rc = subprocess.Popen(args, shell=False)
                rc.communicate()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def demux(self, name, index, output):
        try:
            if self.status == self.STATUSES["INITIALIZED"]:
                args = ["ffmpeg", "-loglevel", "quiet", "-i", name, "-map", "0:{}".format(index), "-c", "copy", output]
                print(args)
                rc = subprocess.Popen(args, shell=False)
                rc.communicate()

                return output
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_language_index(self, language):
        try:
            if self.status == self.STATUSES["INITIALIZED"] and self.streams:
                index = -1
                f_sub = -1
                for i in self.streams["streams"]:
                    if i["codec_type"] == "subtitle":
                        if f_sub == -1:
                            f_sub = i["index"]
                        if "language" in i["tags"].keys():
                            if i["tags"]["language"] == language:
                                print(i["tags"]["language"], "|", i["index"])
                                index = i["index"]
                                return index
                if f_sub > -1:
                    return f_sub
                else:
                    return -1
            else:
                return -1
        except Exception as e:
            print(e)
            return -1

    def get_number_subs(self):
        try:
            if self.status == self.STATUSES["INITIALIZED"]:
                subs = 0
                for i in self.streams["streams"]:
                    if i["codec_type"] == "subtitle":
                        subs += 1
                return subs
            else:
                return 0
        except Exception as e:
            print(e)
            return 0

    def set_file(self, f):
        try:
            info = json.loads(subprocess.check_output(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", f]))
            self.streams = info
            self.status = self.STATUSES["INITIALIZED"]
            return True
        except Exception as e:
            print(e)
            return False

    def remove_file(self):
        try:
            self.streams = None
            self.file = None
            self.status = self.STATUSES["NOFILE"]
            return True
        except Exception as e:
            print(e)
            return False