# -*- encoding: utf-8 -*-
import subprocess
import os
import os.path

# 执行powershell命令
def invoke_powershell(commands,creationflags=subprocess.CREATE_NEW_CONSOLE):
    if os.path.exists("c:\\windows\\system32\\WindowsPowerShell\\v1.0"):
        out = subprocess.Popen(['c:\\windows\\system32\\WindowsPowerShell\\v1.0\\powershell',commands],
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT,
        creationflags=creationflags)
        stdout,error = out.communicate()
        return stdout,error
    else:
        return FileNotFoundError