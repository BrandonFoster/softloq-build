from softloq_build.command_line import cli
import sys
def test_shell_option_incorrect_params():
	assert cli.run_option(['--shell', 'arg']) == cli.INCORRECT_OPTION_PARAMS_ERROR

def test_shell_option_and_exit():
	sys.stdin = open('tests/resources/shell_mode_exit_input.txt', 'r')
	assert cli.run_option(['--shell']) == 0
