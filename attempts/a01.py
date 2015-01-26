
def infinite():
	crash_list = list()
	return crash_list[0]

try:
	infinite()
except IndexError:
	infinite()
