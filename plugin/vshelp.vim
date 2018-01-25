" Some helpers for visual studio
"
if !has("win32") || exists("g:loaded_vshelp")
	finish
endif
let g:loaded_vshelp = 1


function! s:OpenInVisualStudio()
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

command! VSOpen call s:OpenInVisualStudio()
