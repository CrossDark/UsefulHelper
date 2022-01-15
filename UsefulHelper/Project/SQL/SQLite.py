import sqlite3
import os
from UNKnownDB.DB.LightDB import Data


class Build:
    def __init__(self):
        super(Build, self).__init__()
        with Data(path='./') as db:
            os.mkdir('./' + db)
            sqlite3.connect('./' + db + 'data')
