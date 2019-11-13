ECHO 欢迎安装KylinDealer
ECHO 即将弹出依赖库安装，请在弹出窗口中点击下一步安装Python3到您的系统
PAUSE
START python_installer.exe
ECHO 安装Python完成，下一步，安装依赖库
PAUSE
START pip install --user -r requirement.txt
ECHO 安装完成！