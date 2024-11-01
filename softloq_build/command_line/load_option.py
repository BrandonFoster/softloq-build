from typing import Final
import os

TARGET_FILE_DOES_NOT_EXISTS_ERROR: Final[int] = 1
EXPECTED_JSON_TARGET_FILE_ERROR: Final[int] = 2

def option(folder_path: str, target_file: str) -> int:
	target_file_path: str = os.path.abspath(os.path.join(folder_path, target_file))
	if not os.path.isfile(target_file_path):
		print_error(TARGET_FILE_DOES_NOT_EXISTS_ERROR, target_file_path)
		return TARGET_FILE_DOES_NOT_EXISTS_ERROR
	if not target_file_path.lower().endswith('.json'):
		print_error(EXPECTED_JSON_TARGET_FILE_ERROR, target_file_path)
		return EXPECTED_JSON_TARGET_FILE_ERROR
	return 0

def print_error(retval: int, error_info: str = ''):
	error: str = ''
	if retval == TARGET_FILE_DOES_NOT_EXISTS_ERROR: error = 'target-file does not exists:'
	elif retval == EXPECTED_JSON_TARGET_FILE_ERROR: error = 'target-file extension must be .json:'
	if retval > 0: print('<load-option error>', error, error_info, '(use --help for usage guidelines)')