@echo off
@REM Windwos 系統中，使用 anaconda 管理虛擬環境，使用這個批次檔，方便執行多個不同的 env 下的 python 腳本
@REM 這個批次檔可以放在系統的路徑裏面 下方要設定 anaconda 相關路徑(2 擇 1)
@REM 使用方式 pyenv env_name python_script.py
@REM 如果你不是使用 anaconda 要依據你的相關執行環境修改或增設變數
set env_name=%1

if not defined env_name (
    echo Please provide an environment name.
    exit /b 1
)

@REM 如果直接在批次檔裏面設定路徑 這2個方式擇1即可
@REM set anaconda_path=D:\somewhere
@REM 如果使用系統進階選項的環境變數設定了 AnacondaPath 的路徑
set anaconda_path=%AnacondaPath%    
set activater_path=%anaconda_path%\Scripts
set env_path=%anaconda_path%\envs\%env_name%
set python_path=%env_path%

if not exist "%env_path%" (
    @REM echo "%AnacondaPath%"
    @REM echo "%env_path%"
    echo Environment "%env_name%" not found.
    exit /b 1
)

@REM 如果 python 無法執行的話 可能要啟用這個設定
@REM call "%activater_path%\activate.bat" %env_name%
shift
%python_path%\python %python_path%\%1 %*
