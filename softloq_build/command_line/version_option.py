from datetime import datetime
from .. import app_info

def option() -> None:
	print(app_info.GITHUB,
	      f'{app_info.NAME} ver {app_info.VERSION} developed by {app_info.AUTHOR}',
	      f'open-source software {datetime.now().year}, MIT License',
	      sep = '\n')
