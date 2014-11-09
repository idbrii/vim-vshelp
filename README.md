vim-vshelp
==========

A simple plugin for working with Visual Studio

vshelp is a low-tech alternative to vim-scripts/visual_studio.vim. Instead of
using fancy mechanisms to communicate with Visual Studio, it just invokes
devenv.exe with parameters that will change a running Visual Studio's state.
This means that there's a lot of fancy stuff that you can't do (like kicking
off a build), so instead it provides a template for how to kick off a build
from vim with msbuild!

I spend most of my time in vim, so I prefer to build and fix errors in vim
instead of Visual Studio.



Features
========

To open the active vim file in Visual Studio

    :VSOpen

To build C++, add this to ~/.vim/after/ftplugin/cpp.vim

    compiler msvc
    set makeprg=~/.vim/bundle/vshelp/scripts/lib_build.cmd

To build C#, add this to ~/.vim/after/ftplugin/cs.vim

    compiler cs
    set makeprg=~/.vim/bundle/vshelp/scripts/lib_build.cmd

Or create your own copy of lib_build and customize it to your environment.



Recommended
===========

Using idbrii/AsyncCommand with vshelp will make :VSOpen asynchronous.
