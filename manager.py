import os
import sys


class Manager:
    def __init__(self):
        self.CLEAR = ("clear" if os.name == 'posix' else "cls")
        self.all_args = sys.argv[:]

    def show_help(self):
        print(f'''You have not given a valid command for the script!

All avaliable command -->
    ( command name ) --> ( description )
    
    make <name> --> Make a new project with <name>
              ''')

    def _show_help(self):
        self.show_help()
        sys.exit()

    def _parse_args(self):
        self.file_name = self.all_args[0]
        try:
            # Main command check
            self.action = self.all_args[1]

            # Other Argument Checks
            if self.action == 'make':
                try:
                    self.make_name = self.all_args[2]
                except IndexError:
                    self._show_help()

        except IndexError:
            self._show_help()

        if self.action == 'make':
            self.make(name=self.make_name)

    def make(name):
        parent_dir = os.getcwd()

        os.mkdir()

    def run(self):
        os.system(self.CLEAR)
        self._parse_args()


Manager().run()
