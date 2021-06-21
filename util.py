import sys
import os
import time

def key_pressed():
    try:
        import tty, termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def get_input(label,new_lines=2):
    new_lines = "\n" * new_lines
    user_input = input(f"{new_lines}    {label}: ")
    return user_input

def press_any_button(new_lines = 0,indent=4):
    new_lines = "\n" * new_lines
    if os.name == "nt":
        print(f"{new_lines}{indent*' '}Press any key to continue . . .")    
        os.system("pause >nul")
    else:
        input(f"{new_lines}Press enter to continue! ")
        
