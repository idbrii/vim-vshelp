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
import subprocess

try:
    import pywintypes
    import win32com.client
except ImportError:
    pywintypes = None

def _find_latest_devenv():
    cmd = "C:/Program Files (x86)/Microsoft Visual Studio/2017/Professional/Common7/ide/"
    if os.path.exists(cmd):
        return cmd

    versions = (9, 11, 12, 14)
    for v in versions:
        cmd = "c:/Program Files (x86)/Microsoft Visual Studio {version}.0/Common7/ide/".format(version=v)
        if os.path.exists(cmd):
            return cmd

    return ""


def _open_with_batch(filename, line):
    cmd = [os.path.join(_find_latest_devenv(), "devenv")]
    cmd.extend([
        f'/Edit {filename}',
        # Edit.Goto always results in a new VS instance and an error.
        # f'/Command Edit.GoTo {line}',
    ])
    ret = subprocess.call(cmd)
    if ret != 0:
        print("devenv.exe invocation failed: {code}".format(code=ret))


def open_in_visualstudio(filename, line, column):
    if not pywintypes:
        print("Don't have win32com + pywintypes installed (falling back to cmdline):")
        _open_with_batch(filename, line)
        return

    dte = None
    try:
        dte = win32com.client.GetActiveObject("VisualStudio.DTE")

    except pywintypes.com_error as err:
        print("Failed to get handle to Visual Studio (falling back to cmdline):")
        print(err)
        _open_with_batch(filename, line)

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

