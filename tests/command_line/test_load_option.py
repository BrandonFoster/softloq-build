from softloq_build.command_line import cli
from softloq_build.command_line import load_option
def test_load_option_one_param_should_fail():
	assert cli.run_option(['--load', 'targets']) == cli.INCORRECT_OPTION_PARAMS_ERROR

def test_load_option_three_or_more_params_should_fail():
	assert cli.run_option(['--load', 'targets', 'my_target.json', 'random_param1']) == cli.INCORRECT_OPTION_PARAMS_ERROR
	assert cli.run_option(['--load', 'targets', 'my_target.json', 'random_param1', 'random_param2']) == cli.INCORRECT_OPTION_PARAMS_ERROR

def test_load_option_file_does_not_exists():
	assert load_option.option('tests/resources', 'file_does_not_exists.json') == load_option.TARGET_FILE_DOES_NOT_EXISTS_ERROR

def test_load_option_file_not_json():
	assert load_option.option('tests/resources', 'example.notjson') == load_option.EXPECTED_JSON_TARGET_FILE_ERROR

def test_load_option_correct_params():
	assert cli.run_option(['--load', 'tests/resources', 'example.json']) == 0