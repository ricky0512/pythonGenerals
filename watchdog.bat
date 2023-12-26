@echo off
setlocal

rem 每次打執行的指令太長太麻煩了，設一個批次檔來處理 設定資料夾 mydir 變數
set "mydir=D:\anaconda\envs\ems"
set "watchdog=somewhere\watcPath.py"
set "watchDir=C:\somewhere\dir"

rem 使用 mydir 變數
cd /d %mydir%
echo Current working directory: %CD%

rem 在此添加你的執行檔案或其他命令
python %watchdog% %downloadDir%
endlocal
