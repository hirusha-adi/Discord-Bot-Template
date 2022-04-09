from bot.utils.filenames import database

# Users
with open(database.blacklisted_users, "r", encoding="utf-8") as _file:
    blacklisted_users_all_lines_first = _file.readlines()
    blacklisted_users_all_lines = blacklisted_users_all_lines_first


def addUser(user_id):
    if not(user_id in blacklisted_users_all_lines):
        blacklisted_users_all_lines.append(user_id)
        _updateUsersListFile()


def _updateUsersListFile():
    if not(len(blacklisted_users_all_lines_first) == len(blacklisted_users_all_lines)):
        blacklisted_users_all_lines_first = blacklisted_users_all_lines
        with open(database.blacklisted_users, "w", encoding="utf-8") as _file:
            for line in blacklisted_users_all_lines:
                _file.write(str(line))


# Guilds
with open(database.blacklisted_guilds, "r", encoding="utf-8") as _file:
    blacklisted_guilds_all_lines_first = _file.readlines()
    blacklisted_guilds_all_lines = blacklisted_guilds_all_lines_first


def addGuild(guild_id):
    if not(guild_id in blacklisted_guilds_all_lines):
        blacklisted_guilds_all_lines.append(guild_id)
        _updateGuildListFile()


def _updateGuildListFile():
    if not(len(blacklisted_guilds_all_lines_first) == len(blacklisted_guilds_all_lines)):
        blacklisted_guilds_all_lines_first = blacklisted_guilds_all_lines

        with open(database.blacklisted_guilds, "w", encoding="utf-8") as _file:
            for line in blacklisted_guilds_all_lines:
                _file.write(str(line))
