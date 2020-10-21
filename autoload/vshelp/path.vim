if exists('&shellslash')
    function! vshelp#path#expand_as_unix_path(path)
        let shellslash_bak = &shellslash
        let &shellslash = 1
    
        let p = expand(a:path)
    
        let &shellslash = shellslash_bak
        return p
    endf

else
    function! vshelp#path#expand_as_unix_path(path)
        return expand(a:path)
    endf
endif
