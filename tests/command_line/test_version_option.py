from softloq_build.command_line import cli
def test_version_option_incorrect_params():
	assert cli.run_option(['--version', 'arg']) == cli.INCORRECT_OPTION_PARAMS_ERROR

def test_version_option_no_params():
	assert cli.run_option(['--version']) == 0