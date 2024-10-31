from typing import Final
from . import help_option
from . import version_option
from . import shell_mode

KNOWN_OPTIONS: Final[set[str]] = {'--help', '--version', '--shell'}
PRIMARY_OPTIONS: Final[set[str]] = {'--help', '--version', '--shell'}


UNKNOWN_OPTION_ERROR: Final[int] = 1
DUPLICATE_OPTION_ERROR: Final[int] = 2
SHELL_MODE_ONLY_OPTION_ERROR: Final[int] = 3
TWO_PRIMARY_OPTION_ERROR: Final[int] = 4
EXPECTED_OPTION_ERROR: Final[int] = 5
INCORRECT_OPTION_PARAMS_ERROR: Final[int] = 6

def run_option(args: list[str]) -> int:
	"""
	Runs a command-line option with error checking.

	:param args: Represents the command-line option followed by their parameters if any.
	:return: Status code based on the command's success. Shell mode will always return a status code of 0.
	"""

	known_options: set[str] = KNOWN_OPTIONS | shell_mode.KNOWN_OPTIONS
	primary_options: set[str] = PRIMARY_OPTIONS | shell_mode.PRIMARY_OPTIONS

	option_params_dict: dict[str, list[str]] = {}
	option: str | None = None
	primary_option: str | None = None
	for arg in args:
		# found an option
		if arg.find('--') == 0:
			option = arg

			# error checking
			if option not in known_options:
				print_error(UNKNOWN_OPTION_ERROR, option)
				return UNKNOWN_OPTION_ERROR
			elif option in option_params_dict:
				print_error(DUPLICATE_OPTION_ERROR, option)
				return DUPLICATE_OPTION_ERROR
			elif option in shell_mode.PRIMARY_OPTIONS and not shell_mode.is_running():
				print_error(SHELL_MODE_ONLY_OPTION_ERROR, option)
				return SHELL_MODE_ONLY_OPTION_ERROR
			elif option in primary_options:
				if primary_option is not None:
					print_error(TWO_PRIMARY_OPTION_ERROR, ','.join([primary_option, option]))
					return TWO_PRIMARY_OPTION_ERROR
				primary_option = option

			# setting option in dictionary
			option_params_dict[option] = []

		# error: found parameter before a option
		elif option is None:
			print_error(EXPECTED_OPTION_ERROR)
			return EXPECTED_OPTION_ERROR

		# append parameter to recent option
		else: option_params_dict[option].append(arg)

	if primary_option is None:
		print_error(EXPECTED_OPTION_ERROR)
		return EXPECTED_OPTION_ERROR

	return process_option(option_params_dict)

def process_option(option_params_dict: dict[str, list[str]]) -> int:
	for option in option_params_dict:
		if '--version' == option:
			params: list[str] = option_params_dict[option]
			if len(params) > 0:
				print_error(INCORRECT_OPTION_PARAMS_ERROR, '--version')
				return INCORRECT_OPTION_PARAMS_ERROR
			version_option.option()
			return 0
		elif '--help' == option:
			params: list[str] = option_params_dict[option]
			if len(params) > 0:
				print_error(INCORRECT_OPTION_PARAMS_ERROR, '--help')
				return INCORRECT_OPTION_PARAMS_ERROR
			help_option.option()
			return 0
		elif '--shell' == option:
			params: list[str] = option_params_dict[option]
			if len(params) > 0:
				print_error(INCORRECT_OPTION_PARAMS_ERROR, '--shell')
				return INCORRECT_OPTION_PARAMS_ERROR
			elif shell_mode.is_running():
				print('user is now in shell mode (type exit to leave)')
				return 0
			shell_mode.run_sh()
			return 0

		# process shell mode option
		if not shell_mode.is_running(): continue
		if '--exit' == option:
			params: list[str] = option_params_dict[option]
			if len(params) > 0:
				print_error(INCORRECT_OPTION_PARAMS_ERROR, '--shell')
				return INCORRECT_OPTION_PARAMS_ERROR
			shell_mode.exit_sh()
			return 0

	print_error(EXPECTED_OPTION_ERROR)
	return EXPECTED_OPTION_ERROR

def print_error(retval: int, error_info: str = ''):
	error: str = ''
	if retval == UNKNOWN_OPTION_ERROR: error = 'unknown option:'
	elif retval == DUPLICATE_OPTION_ERROR: error = 'duplicate option:'
	elif retval == SHELL_MODE_ONLY_OPTION_ERROR: error = 'option is available only in shell mode:'
	elif retval == TWO_PRIMARY_OPTION_ERROR: error = 'expected only one of these options:'
	elif retval == EXPECTED_OPTION_ERROR: error = 'expected an option as the first argument'
	elif retval == INCORRECT_OPTION_PARAMS_ERROR: error = 'incorrect parameter(s):'

	if retval > 0: print('<cli error>', error, error_info, '(use --help for usage guidelines)')