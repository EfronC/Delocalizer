import subprocess
import sys
import json


class Merger:

    TASKS = {"demux":1, "mux":2}

    def __init__(self):
        self.status = 0
        self.finished = "./Finished"
        self.streams = None

    def get_streams(self, fname):
        try:
            info = json.loads(subprocess.check_output(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", fname]))
            self.streams = info
            return info
        except Exception as e:
            print(e)
            return False

    def mux(self, f, subtitle, params):
        try:
            #ads = ["-metadata:s:s:{}".format(sfiles), "language=eng", "-metadata:s:s:{}".format(sfiles), "handler_name=English", "-metadata:s:s:{}".format(sfiles), "title=Unlocalized", "-max_interleave_delta", "0", "-disposition:s:0", "0", "-disposition:s:{}".format(sfiles), "default", newfilename]
            args = ["ffmpeg", "-loglevel", "quiet", "-y", "-i", f, "-i", subtitle, "-c", "copy", "-map", "0", "-map", "1"] + params
            rc = subprocess.Popen(args, shell=False)
            rc.communicate()

            return True
        except Exception as e:
            print(e)
            return False

    def demux(self, name, index, output):
        try:
            args = ["ffmpeg", "-loglevel", "quiet", "-i", name, "-map", "0:{}".format(index), "-c", "copy", output]
            print(args)
            rc = subprocess.Popen(args, shell=False)
            rc.communicate()

            return output
        except Exception as e:
            print(e)
            return False

    def get_language_index(self, language):
        try:
            if self.streams:
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
                print("Streams not setted")
                return -1
        except Exception as e:
            print(e)
            return -1

    def get_number_subs(self):
        try:
            subs = 0
            for i in self.streams["streams"]:
                if i["codec_type"] == "subtitle":
                    subs += 1
            return subs
        except Exception as e:
            print(e)
            return 0