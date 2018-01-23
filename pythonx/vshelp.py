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

import os

import pywintypes
import win32com.client

def open_in_visualstudio(filename, line, column):
    dte = None
    try:
        dte = win32com.client.GetActiveObject("VisualStudio.DTE")

    except pywintypes.com_error as err:
        print("Failed to get handle to Visual Studio:")
        print(err)

    if dte:
        try:
            dte.ItemOperations.OpenFile(filename)
            dte.ActiveDocument.Selection.MoveToLineAndOffset(line, column+1)
            dte.MainWindow.Activate

        except pywintypes.com_error as err:
            print("Failed to open file: "+ filename)
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
    # Let python deal with escaping.
    filename = filename.replace('\\', '')
    filename = os.path.abspath(filename)

    # print(filename, line, column)
    return open_in_visualstudio(filename, line, column)


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    line = int(sys.argv[2])
    column = int(sys.argv[3])
    open_in_visualstudio(filename, line, column)

