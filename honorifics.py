import pysubs2
import json
import re
import os

class HonorificFixer:
	def __init__(self):
		self.ACCEPTED_STYLES = ["Subtitle", "Regular", "Alt"]
		self.TOKENS = []
		self.HONOR = {
			"kun": [],
			"chan": [],
			"senpai": [],
			"sensei": ["Teacher", "Master", "Doctor", "Professor"],
			"dono": [],
			"san": ["Mr.", "Ms.", "Miss", "Mister"],
			"sama": ["Lady", "Lord", "Sir", "Ma'am"],
			"nee": ["Big sis", "Sis"],
			"onee": ["Big sis", "Sis"],
			"neechan": ["Big sis", "Sis"],
			"oneechan": ["Big sis", "Sis"],
			"neesan": ["Big sis", "Sis"],
			"oneesan": ["Big sis", "Sis"],
			"nii": ["Bog bro", "Bro"],
			"onii": ["Big sis", "Sis"],
			"niichan": ["Big sis", "Sis"],
			"oniichan": ["Big sis", "Sis"],
			"niisan": ["Big sis", "Sis"],
			"oniisan": ["Big sis", "Sis"]
		}

	def load_json(self, name):
		f = open(name, encoding="utf-8")
		jfile = json.load(f)

		return jfile

	def save_result(self, result, name):
		with open(name, "w", encoding="utf8") as output:
			json.dump(result, output, ensure_ascii=False, indent=2)

	def load_subs(self, file):
		subs = pysubs2.load(file, encoding="utf-8")

		return subs

	def compare_styles(self, style: str):
		for i in self.ACCEPTED_STYLES:
			if style.startswith(i):
				return True
		return False

	def find_exact_name_in_string(self, name, string):
		pattern = r"\b" + re.escape(name) + r"\b"
		return bool(re.search(pattern, string, flags=re.I))

	def check_tokens(self, text):
		for i in self.TOKENS:
			if self.find_exact_name_in_string(i, text):
				return True
		return False

	def sanitize_string(self, string):
		# Match substrings enclosed in {}
		pattern = r"\{([^{}]*)\}"

		# Replace all occurrences of the pattern using the replace function
		result = re.sub(pattern, " ", string)
		result = re.sub(r"\\.", " ", result)
		return result

	def reduce_subs(self, subs):
		lines = []
		for nl, line in enumerate(subs):
			if line.type == "Dialogue":
				if self.compare_styles(line.style):
					txt = self.sanitize_string(line.text)
					if self.check_tokens(txt):
						lines.append({"text": txt, "nl": nl, "original": line.text})
			# 	line.text = new_lines[str(nl+1)]

		return lines

	def tokenize(self, words):
		tokens = list()
		for i in words:
			for j in i.split(" "):
				tokens.append(j)

		return set(tokens)

	# Compare subs
	def compare_subs(self, en, es):
		if len(en) == len(es):
			for i,j in zip(en, es):
				for h in self.search_tokens(j["text"]):
					if "-" in h:
						name = self.clean_left(h.split("-")[-2])
						honorific = self.clean_right(h.split("-")[-1])

						new_word = name+"-"+honorific

						if not new_word in i["text"]:
							i["text"] = self.replace_word(name, new_word, i["text"])
							i["text"] = self.replace_english_honorifics(i["text"])
		else:
			print("Difference in lines detected")
			self.save_result({"es": es, "en": en}, "debug.json")
			return False

		return en

	def search_tokens(self, text):
		for i in text.split(" "):
			if self.check_tokens(i):
				yield i

	def clean_left(self, word):
		r = ""
		for i in word[::-1]:
			if i.isalpha():
				r += i
			else:
				break

		return r[::-1]

	def clean_right(self, word):
		r = ""
		for i in word:
			if i.isalpha():
				r += i
			else:
				break

		return r

	def replace_word(self, k,v, text):
		return re.sub(k, v, text, flags=re.I)

	def replace_english_honorifics(self, text, honorific=""):
		honorifics = ["Mr.", "Ms.", "Miss", "Mister", "Lady", "Lord", "Big sis", "Big bro"]
		for i in honorifics:
			text = self.replace_word(i, "", text)

		return text

	def rewrite_dict(self,data):
		return {str(x['nl']): x['text'] for x in data}

	def modify_subs(self, subfile, changes):
		try:
			changes = self.rewrite_dict(changes)
			subs = pysubs2.load(subfile,encoding='utf-8')
			nfilename = "Modified_"+subfile
			for nl, line in enumerate(subs):
				if str(nl) in changes.keys():
					print("Changing:",line.text,"for",changes[str(nl)])
					line.text = changes[str(nl)]
			subs.save(nfilename)
			return nfilename
		except Exception as e:
			print(e)
			return False

	def main(self):
		print("Start")
		os.chdir('./Subs')
		jfile = self.load_json("mato.json")
		self.TOKENS = self.tokenize(jfile.keys())

		subs = self.load_subs("./[EMBER] Mato Seihei no Slave - 06.ass")
		lines = self.reduce_subs(subs)
		lines_en = lines
		#save_result({"lines": lines}, "Eng_result.json")

		subs = self.load_subs("./[DantalianSubs] Mato Seihei no Slave - 06.ass")
		lines = self.reduce_subs(subs)
		lines_es = lines
		#save_result({"lines": lines}, "Esp_result.json")

		changes = self.compare_subs(lines_en, lines_es)
		if changes:
			self.modify_subs("[EMBER] Mato Seihei no Slave - 06.ass", changes)
		#self.save_result({"lines": self.compare_subs(lines_en, lines_es)}, "[EMBER] Mato Seihei no Slave - 05.json")

if __name__ == '__main__':
	honor = HonorificFixer()
	honor.main()