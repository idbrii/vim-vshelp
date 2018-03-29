" Some helpers for visual studio
"
if !has("win32") || exists("g:loaded_vshelp")
	finish
endif
let g:loaded_vshelp = 1


command! VSOpen call vshelp#OpenInVisualStudio()
