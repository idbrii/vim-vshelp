#! /usr/bin/env python
#
# Open file in Visual Studio
# Source: https://stackoverflow.com/a/33244420/79125
#
# Requires pywin32:
# python -m pip install pypiwin32

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import win32com.client

# filename = sys.argv[1]
# line = int(sys.argv[2])
# column = int(sys.argv[3])

def open_in_visualstudio(filename, line, column):
    dte = win32com.client.GetActiveObject("VisualStudio.DTE")

    dte.MainWindow.Activate
    dte.ItemOperations.OpenFile(filename)
    dte.ActiveDocument.Selection.MoveToLineAndOffset(line, column+1)

# Expects three local variables:
# "filename", "line", "column"
def vim_open_in_visualstudio():
    import vim

    args = {}
    for a in ["filename", "line", "column"]:
        args[a] = vim.eval("l:"+ a)

    for a in ["line", "column"]:
        args[a] = int(args[a])

    filename, line, column = args['filename'], args['line'], args['column']

    # print(filename, line, column)
    return open_in_visualstudio(filename, line, column)
