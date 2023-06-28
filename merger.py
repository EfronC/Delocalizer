#Imports


class Merger:

    TASKS = {"demux":1, "mux":2}

    def __init__(self):
        self.status = 0
        self.finished = "./Finished"

    def get_streams(self, fname):
        try:
            info = json.loads(subprocess.check_output(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", fname]))
            return info
        except Exception as e:
            print(e)
            return False

    def shift_subs(fname, delta):
        try:
            subs1 = pysubs2.load(fname, encoding="utf-8")
            subs1.shift(s=delta)
            msub = "m_" + fname
            subs1.save(msub)

            return msub
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
            # filename = os.path.splitext(name)[0]
            # subtitle = filename+".ass"

            args = ["ffmpeg", "-loglevel", "quiet", "-i", name, "-map", "0:{}".format(index), "-c", "copy", output]
            rc = subprocess.Popen(args, shell=False)
            rc.communicate()

            return output
        except Exception as e:
            print(e)
            return False