import subprocess, os, glob
from colorama import init
from termcolor import colored
import logging, pyautogui
init()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Notebook:
    def write(fname=None):
        try:
            if fname ==  None:
                fname = input('filename: ')
            if fname == "":
                pass
            elif os.path.isfile(fname) == False:
                print(f'{fname} does NOT exist.')
            else:
                with open("misc/files_opened.txt", "a") as write:
                    write.write(f"{fname} \n")
                with open("misc/files_opened.txt", "r") as read:
                    lines = read.readlines()
                    lines = set(lines)
                with open("misc/files_opened.txt", "w") as rm_dup:
                    rm_dup.writelines(lines)

                print('0. Welcome back to Notebook! ')
                f =  open(f"{fname}", "r")
                lines = f.readlines()

                if not os.stat(f"{fname}").st_size == 0:
                    for i, e in enumerate(lines):
                        print(f'> {e}')
                while True:
                    myit = range(100)
                    for i, e in enumerate(myit):
                        i = i + 1
                        notes = input(f'{i}.')
                        if i == 100:
                            input("You've hit the limit of 100, starting a new section")
                        if notes == "quit()":
                            return
                        f = open(f'{fname}', 'a')
                        f.write(f"{notes} \n")
        except Exception as e:
            print(e)

    def read():
        try:
            fname = input('filename: ')
            if fname == "":
                pass
            elif os.path.isfile(fname) == False:
                print(f'{fname} does NOT exist.')
            else:
                f = open(f'{fname}', 'r')
                stuff = f.read()
                print(f"""
----- BEGIN {fname.upper()} BLOCK -----
{stuff.strip()}
----- END {fname.upper()} BLOCK -----
""")

        except Exception as e:
            print(e)

    def remove_info():
        try:
            fname = input('filename: ')
            if fname == "":
                pass
            elif os.path.isfile(fname) == False:
                print(f'{fname} does NOT exist.')
            else:
                open(f'{fname}', 'w').close()

        except Exception as e:
            print(e)

    def create_file():
        try:
            fname = input('filename: ')
            if fname == "":
                pass
            elif os.path.isfile(fname) == True:
                print(f'{fname} already exists.')
            else:
                os.system(f'touch {fname}')
                print(f'Created {fname}')
                Notebook.write(fname)
        except Exception as e:
            print(e)

    def remove_file():
        try:
            fname = input('filename: ')
            if fname == "":
                pass
            elif os.path.isfile(fname) == False:
                print(f'{fname} does NOT exist.')

            with open("misc/config.txt", "r+") as f:
                lines = f.readlines()
                line = lines[1]
                EnaDisOpt = line.split(":")
            if EnaDisOpt[1].strip() == "Disabled":
                os.system(f'rm {fname}')
            elif EnaDisOpt[1].strip() == "Enabled":
                    os.system(f"cp {fname} deleted_files")
                    os.system(f'rm {fname}')
                    print("Check deleted_files directory")
            else:
                raise Exception("configurations not set properly")
        except Exception as e:
            print(e)

    def cmd():
        while True:
            try:
                command = input("CMD: ")
                if command == "quit()":
                    return
                os.system(command)
            except Exception as e:
                print(f"Error: {e}")

    def recent_file():
        list_of_files = glob.glob('*') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print(f" Recent opened: {latest_file}")
    def files_opened():
        with open("misc/files_opened.txt", "r") as f:
            lines = f.readlines()
            for i, e in enumerate(reversed(lines)):
                i += 1
                print(f'{i}. {e.strip()} \n')
    def base_item(config_line):
        with open("misc/config.txt", "r+") as f:
            lines = f.readlines()
            line = lines[config_line]
            EnaDisOpt = line.split(":")
            return EnaDisOpt
    def config(passed_item=None):
        try:
            with open("misc/config.txt", "r+") as f:
                lines = f.readlines()
                line = lines[0]
                EnaDisOpt = line.split(":")
                print(f"Reminder | Type options reminder | {EnaDisOpt[1].strip()}")
                line = lines[1]
                EnaDisOpt = line.split(":")
                print(f"Cache_files | Cache removed files | {EnaDisOpt[1].strip()} \n")
                print("Type in the Item you want to Disable/Enable. \n")
            item = input("Item: ")
            item = item.lower().strip()
            if item == "":
                return
            if item == "reminder":
                with open('misc/config.txt', 'r') as file:
                    data = file.readlines()
                passed_item = Notebook.base_item(0)
                if passed_item[1].strip() != "Disabled":
                    data[0] = "Reminder : Disabled\n"
                    with open('misc/config.txt', 'w') as file:
                        file.writelines(data)
                elif passed_item[1].strip() != "Enabled":
                    data[0] = "Reminder : Enabled\n"
                    with open('misc/config.txt', 'w') as file:
                        file.writelines(data)
            elif item == "cache_files":
                with open('misc/config.txt', 'r') as file:
                    data = file.readlines()
                passed_item = Notebook.base_item(1)
                if passed_item[1].strip() != "Disabled":
                    data[1] = "Cache_files : Disabled\n"
                    with open('misc/config.txt', 'w') as file:
                        file.writelines(data)
                elif passed_item[1].strip() != "Enabled":
                    data[1] = "Cache_files : Enabled\n"
                    with open('misc/config.txt', 'w') as file:
                        file.writelines(data)

            else:
                print("Item is not an option")
        except Exception as e:
            pass

def logger():
    logging.basicConfig(filename='misc/app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('Notebook Handler Application Running! \n')
    logging.getLogger().setLevel(logging.DEBUG)


def options():
    while True:
        action = str("""
FILE CONTENTS
write       | Write to a file
read        | Read a file
remove_info | Delete a file info

FILE ITSELF
create | Create a new file
remove | Remove an existing file
recent | Recent files opened
files  | Files opened

MISC
config | Configurations
cmd    | Command prompt
clear  | Clear manually
""")

        with open("misc/config.txt", "r+") as f:
            lines = f.readlines()
            line = lines[0]
            EnaDisOpt = line.split(":")
        if EnaDisOpt[1].strip() == "Disabled":
            pass
        elif EnaDisOpt[1].strip() == "Enabled":
            print('Type options to see the options')
        else:
            raise Exception("configurations not set properly")

        try:
            choice = input(f"{bcolors.FAIL}>>> {bcolors.ENDC}")
        except KeyboardInterrupt:
            exit()
        os.system("clear")

        choice = choice.lower().strip()

        commands = ['write', 'read', 'remove_info', 'create', 'remove', 'cmd', 'files', 'config', 'recent']
        ignore = ['options', "clear"]

        if choice == "options":
            print(action)
        choices = {
        'write': Notebook.write,
        'read': Notebook.read,
        'remove_info': Notebook.remove_info,
        'create': Notebook.create_file,
        'remove': Notebook.remove_file,
        'recent': Notebook.recent_file,
        'cmd': Notebook.cmd,
        'files': Notebook.files_opened,
        'config': Notebook.config,
        }
        if choice == "quit()":
            exit()
        if choice == "clear":
            os.system("clear")
        if choice in commands:
            choices[f'{choice}']()
        elif choice not in commands:
            if choice in ignore:
                pass
            else:
                print(f"'{choice}' is not a command.")

logger()
options()
