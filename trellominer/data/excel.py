"""
Manipulate Excel workbooks.
"""
from datetime import datetime

import openpyxl


class Excel(object):

    def __init__(self):
        self.filename = "platform-engineering-project-register-{0}".format(datetime.strftime("%Y-%m-%d-%H-%M-%S"))

    def filename(self):
        return self.filename

    
