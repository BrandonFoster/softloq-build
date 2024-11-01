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
	                              'The "--" command prefix is optional in shell mode.']],
	               tablefmt = "plain"))
	print()
	print('shell mode options:')
	print(tabulate([['  --exit', 'Exits shell mode.']],
	               tablefmt="plain"))