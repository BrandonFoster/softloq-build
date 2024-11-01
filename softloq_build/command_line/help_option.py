import tabulate
tabulate.PRESERVE_WHITESPACE = True
from tabulate import tabulate

def option() -> None:
	print('usage: softloq-build [options]')
	print()
	print('options:')
	print(tabulate([['  --help', 'Displays the help guideline.'],
	                ['  --version', 'Displays the version.'],
	                ['  --shell', 'Enters shell mode with more options enabled (see below).\n'
	                              'The "--" command prefix is optional in shell mode.'],
	                ['  --load <folder-path> <target-file>', 'Loads the specified target build file into the cache folder.']],
	               tablefmt = "plain"))
	print()
	print('shell mode options:')
	print(tabulate([['  --exit', 'Exits shell mode.']],
	               tablefmt="plain"))