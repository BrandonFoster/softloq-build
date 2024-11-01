import sys
from softloq_build import command_line

def main() -> int:
	"""
	Main entry point of the console application.

	Attempts to run a command-line option if arguments are provided.
	Runs the help option by default.

	:return: Status code from the command-line interface.
	"""

	if len(sys.argv) > 1: return command_line.run_option(sys.argv[1:])
	return command_line.run_option(['--help'])


if __name__ == '__main__': sys.exit(main())