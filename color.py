CSI = "\033["
OSC = '\033]'
BEL = '\a'


def set_title(title):
	return OSC + '2;' + title + BEL

def clear_screen(mode=2):
	return CSI + str(mode) + 'J'

def clear_line(mode=2):
	return CSI + str(mode) + 'K'

def code_to_chars(code):
	return CSI + str(code) + "m"

class AnsiCodes(object):
	def __init__(self):
		for code in dir(self):
			if not code.startswith("_"):
				setattr(self, code, code_to_chars(getattr(self, code)))

class CursorCodes(object):
	def __init__():
		pass
	def UP(self, n):
		return f"{CSI}{n}A"
	def DOWN(self, n):
		return f"{CSI}{n}B"
	def FORWARD(self, n):
		return f"{CSI}{n}C"
	def BACK(self, n):
		return f"{CSI}{n}D"
	def POS(self, row, column):
		return f"{CSI}{row};{column}H"

class ForeCodes(AnsiCodes):
	RESET = 39
	BLACK = 30
	RED = 31
	GREEN = 32
	YELLOW = 33
	BLUE = 34
	MAGENTA = 35
	CYAN = 36
	WHITE = 37
	GRAY = 90
	BRIGHT_RED = 91
	BRIGHT_GREEN = 92
	BRIGHT_YELLOW = 93
	BRIGHT_BLUE = 94
	BRIGHT_MAGENTA = 95
	BRIGHT_CYAN = 96
	BRIGHT_WHITE = 97

class BackCodes(AnsiCodes):
	RESET = 49
	BLACK = 40
	RED = 41
	GREEN = 42
	YELLOW = 43
	BLUE = 44
	MAGENTA = 45
	CYAN = 46
	WHITE = 47
	GRAY = 100
	BRIGHT_RED = 101
	BRIGHT_GREEN = 102
	BRIGHT_YELLOW = 103
	BRIGHT_BLUE = 104
	BRIGHT_MAGENTA = 105
	BRIGHT_CYAN = 106
	BRIGHT_WHITE = 107

class StyleCodes(AnsiCodes):
	RESET_ALL = 0
	BOLD = 1
	DIM = 2
	ITALIC = 3
	UNDERLINE = 4
	BLINK = 5
	STRIKE = 9
	DOUBLE_UNDERLINE = 21

Cursor = CursorCodes()
Fore = ForeCodes()
Back = BackCodes()
Style = StyleCodes()