class codeTranslator:
	code = {}
	# Translates code to english.
	# pre: lowercase string to translate
	# post: returns translated string
	def translate_code(self, code):

		if code == "":
			return "no text"

		if "    " in code:
			code.replace(" ", " ")

		translation = ""
		words = code.split(" ")
		spacer = 0
		for code_word in words:
			chars = code_word.split(" ")
			for char in chars:
				for k, v in self.code.items():
					if char == v:
						translation += k
			translation += " "

		return translation.rstrip()

	# Translates english to code.
	# pre: lowercase string to translate
	# post: returns translated string
	def translate_english(self, text):

		if text == "":
			return "no text"

		translation = ""

		words = text.split(" ")

		for word in words:
			w = list()
			for char in word:
				if char.lower() in self.code:
					w.append(self.code[char.lower()])

			translation += " ".join(w)
			translation += "    "

		return translation.rstrip()

class navajoCodeTranslator(codeTranslator):
	code = {
		"a": "wol-la-chee",
		"b": "shush",
		"c": "moashi",
		"d": "be",
		"e": "dzeh",
		"f": "ma-e",
		"g": "klizzie",
		"h": "lin",
		"i": "tkin",
		"j": "tkele-cho-gi",
		"k": "klizzie-yazzi",
		"l": "dibeh-yazzi",
		"m": "na-as-tso-si",
		"n": "nesh-chee",
		"o": "ne-ash-jsn",
		"p": "bi-sodih",
		"q": "ca-yeilth",
		"r": "gah",
		"s": "dibeh",
		"t": "than-zie",
		"u": "no-da-ih",
		"v": "a-keh-di-glini",
		"w": "gloe-ih",
		"x": "al-an-as-dzoh",
		"y": "tsah-as-zih",
		"z": "besh-do-gliz",
	}

class morseCodeTranslator(codeTranslator):
	
	# International morse code
    morse = {
        # Letters
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        # Numbers
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Punctuation
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
    }
