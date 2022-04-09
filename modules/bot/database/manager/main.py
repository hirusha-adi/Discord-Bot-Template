import json
import bot.utils.filenames as filenames


with open(filenames.Database.main, "r", encoding="utf-8") as _file:
    data = json.load(_file)
prefix = data['prefix']
token = data['token']


class Blacklisted:
    def __init__(self):
        with open(filenames.Database.blacklisted_users, "r", encoding="utf-8") as _file:
            self.blacklisted_users_all_lines_first = _file.readlines()
            self.blacklisted_users_all_lines = self.blacklisted_users_all_lines_first

    def addUser(self, user_id):
        if not(user_id in self.blacklisted_users_all_lines):
            self.blacklisted_users_all_lines.append(user_id)
            self._updateListFile()

    def _updateListFile(self):
        if not(len(self.blacklisted_users_all_lines_first) == len(self.blacklisted_users_all_lines)):

            self.blacklisted_users_all_lines_first = self.blacklisted_users_all_lines
            with open(filenames.Database.blacklisted_users, "w", encoding="utf-8") as _file:
                for line in self.blacklisted_users_all_lines:
                    _file.write(str(line))
