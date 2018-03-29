" Often useful for picking out the this pointer and parameters.
function! vshelp#guess_correct_pointer()
	%smagic/\v(.\u{-}.=.\x+) /\1\r/g
	" Heap pointers on my platform start with the same bitpattern, so they're
	" easy to identify.
	v/07FF/d
	%sort /=/u
endf

function! vshelp#OpenInVisualStudio()
	let pos = getcurpos()
	let line = pos[1]
	let column = pos[2]
	let filename = fnameescape(expand('%:p'))
    python << EOP
try:
    import vshelp
    vshelp.vim_open_in_visualstudio()
except ImportError as err:
    print("ERROR: "+ str(err) +"\n"
    + """vshelp will fail to import when pywintypes fails to import.
Try removing pywin32 and pypiwin32 and then installing pypiwin32 again.
""")
EOP
endfunction

