import subprocess
import sys
import json
import os
import re
import glob
import pysubs2
import argparse
from dotenv import load_dotenv

load_dotenv()

from delocalizer import Delocalizer

LANGUAGES = ["eng", "spa"]
WORDS = {}
ERRORS = []

parser = argparse.ArgumentParser(description='Convert vobsub subtitles into srt format.')
parser.add_argument('--shift', dest='shift', type=float, action="store", default=0.0,
                   help='Shift time')
parser.add_argument('--j', dest='jfile', type=str, action="store", default=False,
                   help='JSON file')
parser.add_argument('--l', dest='language', type=str, action="store", default=False,
                   help='Language')
parser.add_argument('--f', dest='folder', type=str, action="store", default=False,
                   help='Folder')
parser.add_argument('--y', dest='yes', type=int, action="store", default=False,
                   help='Edit the first subtitle track')

def load_json(jname):
	try:
		global WORDS
		print("Loading ", jname)
		f = open(jname)
		data = json.load(f)
		WORDS = data
		return True
	except Exception as e:
		return False


def testsubs(subfile):
	try:
		active = False
		p = 0
		subs = pysubs2.load(subfile,encoding='utf-8')
		with open("test.txt", "w", encoding="utf-8") as f:
			for k,line in enumerate(subs):
				if not active:
					if bool(re.match(r"{\\(.*)(}r$)", line.text, re.IGNORECASE)):
						active = True
						p += 1
						# f.write(str(k)+": "+line.text+"\n")
						# f.write(subs[k+1].text+"\n")
				else:
					if p == 1: #u
						if bool(re.match(r"{\\(.*)(}u$)", line.text, re.IGNORECASE)):
							p += 1
							continue
						else:
							active = False
							p = 0
					elif p == 2: #b
						if bool(re.match(r"{\\(.*)(}b$)", line.text, re.IGNORECASE)):
							p += 1
							continue
						else:
							active = False
							p = 0
					elif p == 3: #b
						if bool(re.match(r"{\\(.*)(}b$)", line.text, re.IGNORECASE)):
							p += 1
							continue
						else:
							active = False
							p = 0
					elif p == 4: #e
						if bool(re.match(r"{\\(.*)(}e$)", line.text, re.IGNORECASE)):
							p += 1
							continue
						else:
							active = False
							p = 0
					elif p == 5: #r
						if bool(re.match(r"{\\(.*)(}r$)", line.text, re.IGNORECASE)):
							p += 1
							subs[k-p].text = subs[k-p].text[:-1] + "G"
							subs[k-(p-1)].text = subs[k-(p-1)].text[:-1] + "o"
							subs[k-(p-2)].text = subs[k-(p-1)].text[:-1] + "m"
							subs[k-(p-3)].text = subs[k-(p-1)].text[:-1] + "u"
							subs[k-(p-4)].text = ""
							subs[k-(p-5)].text = ""
							f.write(str(k)+": "+subs[k-(p-0)].text+"\n")
							f.write(str(k)+": "+subs[k-(p-1)].text+"\n")
							f.write(str(k)+": "+subs[k-(p-2)].text+"\n")
							f.write(str(k)+": "+subs[k-(p-3)].text+"\n")
							f.write(str(k)+": "+subs[k-(p-4)].text+"\n")
							f.write(str(k)+": "+subs[k-(p-5)].text+"\n")
							active = False
							p = 0
						else:
							active = False
							p = 0
	except Exception as e:
		print(e)

def checkCase(k, subs):
	try:
		if bool(re.match(r"{\\(.*)(}u$)", subs[k+1].text, re.IGNORECASE)):
			if bool(re.match(r"{\\(.*)(}b$)", subs[k+2].text, re.IGNORECASE)):
				if bool(re.match(r"{\\(.*)(}b$)", subs[k+3].text, re.IGNORECASE)):
					if bool(re.match(r"{\\(.*)(}e$)", subs[k+4].text, re.IGNORECASE)):
						if bool(re.match(r"{\\(.*)(}r$)", subs[k+5].text, re.IGNORECASE)):
							return 1 # rubber
				elif bool(re.match(r"{\\(.*)(}rub$)", subs[k+3].text, re.IGNORECASE)):
					return 2 # r u b rub
		elif bool(re.match(r"{\\(.*)(}e$)", subs[k+1].text, re.IGNORECASE)):
			if bool(re.match(r"{\\(.*)(}r$)", subs[k+2].text, re.IGNORECASE)):
				if bool(re.match(r"{\\(.*)(}ber$)", subs[k+3].text, re.IGNORECASE)):
					return 3 # b e r ber
		return 0
	except Exception as e:
		raise e

def modifyByCase(k, subs, case):
	try:
		if case == 1:
			subs[k].text = subs[k].text[:-1] + "G"
			subs[k+1].text = subs[k+1].text[:-1] + "o"
			subs[k+2].text = ""
			subs[k+3].text = subs[k+3].text[:-1] + "m"
			subs[k+4].text = subs[k+4].text[:-1] + "u"
			subs[k+5].text = ""

			return 5
		elif case == 2:
			subs[k].text = subs[k].text[:-1] + "G"
			subs[k+1].text = subs[k+1].text[:-1] + "o"
			subs[k+2].text = ""

			return 2
		elif case == 3:
			subs[k].text = subs[k].text[:-1] + "m"
			subs[k+1].text = subs[k+1].text[:-1] + "u"
			subs[k+2].text = ""

			return 2
		else:
			return 0
	except Exception as e:
		print(e)

def modifySubsWAnim(subfile):
	try:
		subs = pysubs2.load(subfile,encoding='utf-8')
		nfilename = "[Delocalized]"+subfile
		active = False
		case = 0
		for nl, line in enumerate(subs):
			if not active:
				if bool(re.match(r"{\\(.*)(}r$)", line.text, re.IGNORECASE)) or bool(re.match(r"{\\(.*)(}b$)", line.text, re.IGNORECASE)):
					case = checkCase(nl, subs)
					if case > 0:
						active = True
						skips = modifyByCase(nl, subs, case)
						continue
				for k,v in WORDS.items():
					if bool(re.match(r"{\\(.*)(}rub$|}ber)", line.text, re.IGNORECASE)):
						nline = line.text
						nline = re.sub(r"rub", "Go", nline, flags=re.I)
						nline = re.sub(r"ber", "mu", nline, flags=re.I)
						line.text = nline
						break
					else:
						line.text = re.sub(k, v, line.text, flags=re.I)
			else:
				skips -= 1
				if skips > 0:
					continue
				else:
					active = False
					case = 0
					continue
		subs.save(nfilename)
		return nfilename
	except Exception as e:
		print(e)
		return False

def modifySubs(subfile):
	try:
		subs = pysubs2.load(subfile,encoding='utf-8')
		nfilename = "[Delocalized]"+subfile
		for nl, line in enumerate(subs):
			for k,v in WORDS.items():
				line.text = re.sub(k, v, line.text, flags=re.I)
		subs.save(nfilename)
		return nfilename
	except Exception as e:
		print(e)
		return False

def extract_subs(name, index, language="eng"):
	try:
		filename = os.path.splitext(name)[0]
		subtitle = filename+".ass"

		args = ["ffmpeg", "-loglevel", "quiet", "-i", name, "-map", "0:{}".format(index), "-c", "copy", subtitle]
		rc = subprocess.Popen(args, shell=False)
		rc.communicate()
		return subtitle
	except Exception as e:
		print(e)
		return False

def shift_subs(fname, delta):
	subs1 = pysubs2.load(fname, encoding="utf-8")
	subs1.shift(s=delta)
	msub = "m_" + fname
	subs1.save(msub)

	return msub

def mux(streams, f, subtitle):
	try:
		sfiles = get_number_subs(streams)

		filename = os.path.splitext(f)[0]
		if os.path.isfile(subtitle):
			newfilename = ".\\Finished\\"+filename + '.mkv'

			args = ["ffmpeg", "-loglevel", "quiet", "-y", "-i", f, "-i", subtitle, "-c", "copy", "-map", "0", "-map", "1", "-metadata:s:s:{}".format(sfiles), "language=eng", "-metadata:s:s:{}".format(sfiles), "handler_name=English", "-metadata:s:s:{}".format(sfiles), "title=Unlocalized", "-max_interleave_delta", "0", "-disposition:s:0", "0", "-disposition:s:{}".format(sfiles), "default", newfilename]
			rc = subprocess.Popen(args, shell=False)
			rc.communicate()

		return True
	except Exception as e:
		return False

def get_streams(fname):
	info = json.loads(subprocess.check_output(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", fname]))
	return info

def get_language_index(streams, language):
	try:
		index = -1
		f_sub = -1
		for i in streams["streams"]:
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
	except Exception as e:
		print(e)
		return -1

def get_number_subs(streams):
	try:
		subs = 0
		for i in streams["streams"]:
			if i["codec_type"] == "subtitle":
				subs += 1
		return subs
	except Exception as e:
		print(e)
		return 0


def demux(language):
	global ERRORS
	files = glob.glob('*.mkv')
	index = -1
	for f in files:
		print("Extracting: ", f)
		streams = get_streams(f)
		index = get_language_index(streams, language)
		if index > -1:
			print("Subtitles found at", index)
			subfile = extract_subs(f, index, language)
			if subfile:
				print("Delocalizing...")
				unloc_sub = modifySubs(subfile)
				if unloc_sub:
					os.remove(subfile)
					print("Muxxing with file:", unloc_sub)
					r = mux(streams, f, unloc_sub)
					if r:
						os.remove(unloc_sub)
					else:
						print("Failed to mux sub!")
						ERRORS.append(str(f))
				else:
					print("Failed to modify subs!")
					ERRORS.append(str(f))
			else:
				print("Failed to extract Subtitle!")
				ERRORS.append(str(f))
		else:
			print("Subtitles not found!")
			ERRORS.append(str(f))
		
		



def main():
	args = parser.parse_args()

	delocalizer = Delocalizer()
	s = delocalizer.prepare_data(args)
	if s:
		delocalizer.delocalize()

def test():
	testsubs("One.Piece.E796-E798.720p.ass")

if __name__ == '__main__':
	main()

#print(mkvmerge)
#f = '.\\Files\\Getsuyoubi no Tawawa 2 - 02.mkv'

#print(info['tracks'])
