:: Generic script template for building Visual Studio projects using MSBuild.
@echo off

title %0 %*

if "%1" == "help" (
	echo lib_build.cmd usage:
	echo Build code for a solution. Unspecified arguments will use defaults.
	echo make [config] [platform] [project] [work_dir] [target]
	echo make Debug pc zelda c:/p4/zelda/game/source/pc zelda_pc
	exit /b 1
)

setlocal

set config=%1
if NOT defined config (
	set config=Debug
)

set sku=%2
if NOT defined sku (
	set sku=pc
)

:: Map sku to VS platform config
set sku_platform=%sku%
if %sku% == pc (
	set sku_platform=x64
) else if %sku% == ps3 (
	set sku_platform=PS3
) else if %sku% == xbox (
	set sku=Durango
	set sku_platform=Durango
) else (
	echo Unknown platform. Using %sku_platform%
)


set project=%3
if NOT defined project (
	:: TODO: Update this with your default project name.
	set project=game_name
)

set work_dir=%4
if NOT defined work_dir (
	:: TODO: Update with the path to your solution.
	set work_dir=c:\p4\%project%\game\source\pc
)

set target=%5
if NOT defined target (
	:: TODO: Update this with your vcxproj/sln naming scheme.
	set target=%project%_%sku%
)

set log_file=%TEMP%\build_%project%_%sku%.log

echo %log_file%(0): Build Started: %DATE% %TIME%

:: TODO: You might want x64 buildchain instead of x86.
call "C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x86 >NUL
pushd %work_dir%

:: /verbosity:quiet - squelch nonessential build output (so we don't see build step errors, etc).
:: /property:GenerateFullPaths=true to make sure we get paths that vim can use.
:: Use tee so we can see the build log while it's building if we want.
:: You may have problems if you have spaces in your Config or platform names.
msbuild /nologo /v:quiet /p:GenerateFullPaths=true /target:%target% /p:Configuration=%config% /p:Platform=%sku_platform% %work_dir%\%target%.sln 2>&1 | tee %log_file%
:: Output logfile so it's in vim quickfix for easy jumping.
echo %log_file%(0): Build Completed: %DATE% %TIME%

popd
