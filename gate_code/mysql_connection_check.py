import MySQLdb
from gate import settings
from time import sleep

db_settings = settings.DATABASES['default']

def mysql_connection_check():
    try:
        con = MySQLdb.connect(
            user    = db_settings["USER"],
            passwd  = db_settings["PASSWORD"],
            host    = db_settings["HOST"],
            port    = db_settings["PORT"],
            db      = db_settings["NAME"]
        )
        con.cursor()
    except Exception:
        return False
    return True

connected = False
for i in range(15):
    connected = connected or mysql_connection_check()
    if connected: 
        break
    print("Wait for connecting Mysql")
    sleep(1)

print("Mysql connectted!" if connected else "Mysql connect Failure")
