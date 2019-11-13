@ECHO off
ECHO 欢迎安装KylinDealer
ECHO 即将弹出依赖库安装，请在弹出窗口中，勾选下方的两个对勾并点击安装
PAUSE
python_installer.exe
ECHO 安装Python完成，下一步，安装依赖库
pip install --user -r requirements.txt
ECHO 安装完成！
PAUSE