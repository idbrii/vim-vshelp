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

import pywintypes
import win32com.client

# filename = sys.argv[1]
# line = int(sys.argv[2])
# column = int(sys.argv[3])

def open_in_visualstudio(filename, line, column):
    try:
        dte = win32com.client.GetActiveObject("VisualStudio.DTE")
        dte.MainWindow.Activate
        dte.ItemOperations.OpenFile(filename)
        dte.ActiveDocument.Selection.MoveToLineAndOffset(line, column+1)
    except pywintypes.com_error as err:
        # Sometimes we get this error:
        #   pywintypes.com_error: (-2147352567, 'Exception occurred.', (0, None, None, None, 0, -2147024809), None)
        # I haven't seen a good reason for it. Maybe we should try to fall back
        # to the old batchfile method?
        print("Failed to get handle to Visual Studio:")
        print(err)


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
