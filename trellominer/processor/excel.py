"""
Manipulate Excel workbooks.
"""
from datetime import datetime
import os

from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font, Border, Side, PatternFill

from trellominer.api import trello


class Excel(object):

    def __init__(self):
        self.filename = os.path.join(os.path.expanduser('~'), "Platform Engineering Projects {0}.xlsx".format(datetime.now().strftime("%Y-%m-%d")))

    def filename(self):
        return self.filename

    def process_boards(self, boards):
        """Creates a series of worksheets in a workbook based on Trello board names."""
        highlight = NamedStyle(name='highlight')
        highlight.font = Font(bold=True, size=20)

        tabletop = NamedStyle(name='tabletop')
        tabletop.font = Font(bold=True, color='FFFFFF')
        bd = Side(style='thin', color="000000", border_style='thin')
        tabletop.border = Border(left=bd, right=bd, top=bd, bottom=bd)
        tabletop.fill = PatternFill("solid", bgColor="333333")

        wb = Workbook()
        wb.add_named_style(highlight)

        lookup = trello.Trello()

        # Dump the default worksheet from the document.
        # TODO: (PS) Is there a better way to handle this?
        for sheet in wb:
            if "Sheet" in sheet.title:
                wb.remove_sheet(sheet)
        for board in boards:
            if "Projects" in board['name']:
                ws = wb.create_sheet(title="{0}".format(board['name']), index=0)
                ws.sheet_properties.tabColor = "0000FF"
            else:
                name = board['name'][0:30]
                ws = wb.create_sheet(title="{0}".format(name), index=None)
            ws['A1'].style = 'highlight'
            ws['A1'] = "{0}".format(board['name'])

            if board['desc']:
                ws['A2'] = "{0}".format(board['desc'])
            else:
                ws['A2'] = "{0}".format('No Project Description')

            ws['A3'] = "{0}".format(board['url'])
            ws['A3'].style = 'Hyperlink'
            ws['A4'] = ""

            headings = ["Name", "Description", "Status", "Due Date", "Complete", "Closed", "Members"]
            ws.append(headings)
            header_row = ws[5]
            for cell in header_row:
                cell.style = tabletop

            cards = lookup.cards(board['shortLink'])

            for card in cards:
                listname = lookup.lists(card['idList'])
                line = [card['name'], card['desc'], listname['name'], card['due'], card['dueComplete'], card['closed']]
                member_list = ""
                for member in card['members']:
                    member_list += "{0},".format(member['fullName'])

                member_list.rstrip(',')
                line.append(member_list)
                ws.append(line)

        wb.save(self.filename)
