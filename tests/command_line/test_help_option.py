from softloq_build.command_line import cli
def test_help_option_incorrect_params():
	assert cli.run_option(['--help', 'arg']) == cli.INCORRECT_OPTION_PARAMS_ERROR

def test_help_option_no_params():
	assert cli.run_option(['--help']) == 0