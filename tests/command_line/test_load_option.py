from softloq_build.command_line import cli
def test_load_option_one_param_should_fail():
	assert cli.run_option(['--load', 'targets']) == cli.INCORRECT_OPTION_PARAMS_ERROR

def test_load_option_three_or_more_params_should_fail():
	assert cli.run_option(['--load', 'targets', 'my_target.json', 'random_param1']) == cli.INCORRECT_OPTION_PARAMS_ERROR
	assert cli.run_option(['--load', 'targets', 'my_target.json', 'random_param1', 'random_param2']) == cli.INCORRECT_OPTION_PARAMS_ERROR

def test_load_option_correct_params():
	assert cli.run_option(['--load', 'targets', 'my_target.json']) == 0