@echo on
chcp 65001

@REM 请设置Python路径。Please set the Python path。
@REM set "python_path=F:\0_DATA\2_CODE\Anaconda\envs\asdTools\python.exe"
set "python_path="

@REM 请设置选项名称。Please set the option name.
set "menu_name=调整图像至256x144"
@REM set "menu_name=ResizeImageTo256x144"

if not exist "%python_path%" set "python_path=F:\0_DATA\2_CODE\Anaconda\envs\asdTools\python.exe"
set "script_dir=%~dp0"
set "script_name=%ContextMenu_ImageResizer_256x144.py"
"%python_path%" "%script_dir%\%script_name%" "%python_path%" "%menu_name%" "%script_dir%"

pause
