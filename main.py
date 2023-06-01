import subprocess
import sys
import json
import os
import glob
import pysubs2

mkvmerge = "C:\\Users\\DrkEfron\\Documents\\Extract\\mkvtoolnix\\mkvmerge.exe"
mkvextract = "C:\\Users\\DrkEfron\\Documents\\Extract\\mkvtoolnix\\mkvextract.exe"

BLEACH_WORDS = [
	["Soul Reaper", "Shinigami"],
	["Spiritual Pressure", "Reiatsu"]
]

def subExtract():
	files = glob.glob(".\\Files\\*.mkv")
	output = []
	#subsfn = []
	for f in files:
		print("File: ", f)
		info = json.loads(subprocess.check_output([mkvmerge, '-J', f]))
		filename = os.path.splitext(f)[0]
		for i in info['tracks']:
			print(i['type'])
			#print(i['track_name'])
			if i['type'] == 'subtitles':
				if i['properties']["track_name"] == 'English' or i['properties']["language"] == 'eng':
					sfn = filename+".ass"
					args = [mkvextract, 'tracks', f, str(i['properties']["number"]-1)+":"+filename+".ass"]
					rc = subprocess.Popen(args, shell=False)
					rc.communicate()
					return sfn

def modifySubs():
	files = glob.glob(".\\Files\\*.ass")
	for f in files:
		subs = pysubs2.load(f,encoding='utf-8')
		filename = os.path.splitext(f)[0].split("\\")[-1]
		for line in subs:
			line.text = line.text.replace("Soul Reaper", "Shinigami")
			line.text = line.text.replace("Spiritual Pressure", "Reiatsu")
		subs.save("./Extracted/[Unlocalized] "+filename+".ass")

# def mux():
# 	files = glob.glob('*.mkv')
# 	for f in files:
# 		filename = os.path.splitext(f)[0]
# 		newfilename = filename + '_Delocalized.mkv'
		#args = [mkvmerge, '--ui-language', 'en', '--output', newfilename, '--no-global-tags', ]


def main():
	sfn = subExtract()
	modifySubs()
	#clean()

if __name__ == '__main__':
	main()

#print(mkvmerge)
#f = '.\\Files\\Getsuyoubi no Tawawa 2 - 02.mkv'

#print(info['tracks'])
