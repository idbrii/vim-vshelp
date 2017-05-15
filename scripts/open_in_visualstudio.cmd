:: Open the input file at the input line.
::
:: Bug: The line doesn't work
::


:: VS2008
"c:\Program Files (x86)\Microsoft Visual Studio 9.0\Common7\ide\devenv" /Edit "%1" /Command "Edit.GoTo %2"
:: VS2012
REM "c:\Program Files (x86)\Microsoft Visual Studio 11.0\Common7\IDE\devenv" /Edit "%1" /Command "Edit.GoTo %2"
:: VS2013
REM "c:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\devenv" /Edit "%1" /Command "Edit.GoTo %2"
:: VS2015
REM "c:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\IDE\devenv" /Edit "%1" /Command "Edit.GoTo %2"



:: TODO: Can I detect which Visual Studio is running? Above is not a great solution. Maybe something like this?
REM :check
REM :: Note: tasklist does not return a valid exit code, so we need to use findstr.
REM tasklist /M UE4Editor-Core.dll | findstr "No tasks" > nul
REM IF ERRORLEVEL 1 (
REM 	IF x%1 NEQ x-f GOTO :check
REM )
