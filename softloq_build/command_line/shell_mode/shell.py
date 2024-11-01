from typing import Final
import shlex
from ...command_line import cli as command_line

KNOWN_OPTIONS: Final[set] = {'--exit'}
PRIMARY_OPTIONS: Final[set] = {'--exit'}

on: bool = False

def is_running() -> bool:
    global on
    return on

def run_sh():
    # welcome message
    command_line.version_option.option()
    print('user is now in shell mode (type exit to leave)')
    
    global on
    on = True
    while on:
        print('softloq-build>', end=' ')
        option: str
        try: option = str(input())
        except KeyboardInterrupt:
            print('^C')
            on = False
            continue
        except EOFError:
            on = False
            continue
        if len(option) == 0: continue
        if option.find('--') != 0: option = '--' + option
        command_line.run_option(shlex.split(option))
    print('exiting the shell mode...')

def exit_sh() -> None:
    global on
    on = False