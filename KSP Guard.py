# ©2021 Joshua Craig

import subprocess
import time
import psutil

ProgramPath = r"C:\Program Files (x86)\Steam\steamapps\common\Ksp RSS_RO\KSP_x64.exe"
ProgramName = "KSP_x64.exe"

while True:
    ProgramOpen = ProgramName in (i.name() for i in psutil.process_iter())

    if not ProgramOpen:
        subprocess.call(ProgramPath)
        print(f"{ProgramName} appears to have closed, restarting...")
    time.sleep(4)
