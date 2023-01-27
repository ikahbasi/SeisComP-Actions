# Seiscomp
class seiscomp_info:
    def __init__(self):
        self.mysql_user = 'sysop'
        self.mysql_pass = 'sysop'
        self.host       = 'localhost'

# Google Gmail
class gmail_info:
    def __init__(self):
        self.user    = 'example@gmail.com'
        self.pwd    = 'ABCDEFGH'


# Cut out
class cutout:
    def __init__(self):
        self.stime = 0
        self.etime = 600
        self.archive = '/media/tdmmo/DataBase1'
