import pysubs2
import json
import re

class HonorificFixer:
	def __init__(self):
		self.ACCEPTED_STYLES = ["Subtitle", "Regular", "Alt"]
		self.TOKENS = []

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

	def check_tokens(self, text):
		for i in self.TOKENS:
			if i in text:
				return True
		return False

	def reduce_subs(self, subs):
		lines = []
		for nl, line in enumerate(subs):
			if line.type == "Dialogue":
				if self.compare_styles(line.style):
					if self.check_tokens(line.text):
						lines.append({"text": line.text, "nl": nl})
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

	def replace_english_honorifics(self, text):
		honorifics = ["Mr.", "Ms.", "Miss", "Mister"]
		for i in honorifics:
			text = self.replace_word(i, "", text)

		return text

	def main():
		jfile = load_json("")
		self.TOKENS = self.tokenize(jfile.keys())

		subs = self.load_subs("./Eng_sub.ass")
		lines = self.reduce_subs(subs)
		lines_en = lines
		#save_result({"lines": lines}, "Eng_result.json")

		subs = self.load_subs("./Esp_sub.ass")
		lines = self.reduce_subs(subs)
		lines_es = lines
		#save_result({"lines": lines}, "Esp_result.json")

		self.save_result({"lines": self.compare_subs(lines_en, lines_es)}, "modified.json")