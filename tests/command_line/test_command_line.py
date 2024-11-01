from softloq_build import command_line
def test_no_unknown_option():
	assert command_line.run_option(['--unknown-command']) == command_line.cli.UNKNOWN_OPTION_ERROR

def test_no_duplicate_options():
	assert command_line.run_option(['--help', '--help']) == command_line.cli.DUPLICATE_OPTION_ERROR

def test_no_primary_option():
	assert command_line.run_option([]) == command_line.cli.EXPECTED_OPTION_ERROR
	assert command_line.run_option(['only_a_parameter']) == command_line.cli.EXPECTED_OPTION_ERROR

def test_no_multiple_primary_option():
	assert command_line.run_option(['--help', '--version']) == command_line.cli.TWO_PRIMARY_OPTION_ERROR

def test_no_shell_mode_only_option_in_disabled_shell_mode():
	assert command_line.run_option(['--exit']) == command_line.cli.SHELL_MODE_ONLY_OPTION_ERROR
