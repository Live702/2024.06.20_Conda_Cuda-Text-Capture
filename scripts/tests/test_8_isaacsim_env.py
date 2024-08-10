import os
import sys
import shutil
path_SystemRoot = os.environ.get('SystemRoot') if os.environ.get('SystemRoot') is not None else "Cant find value"
path_Python     = os.environ.get('PYTHONPATH') if os.environ.get('PYTHONPATH') is not None else "Cant find value"
python_exe_path = shutil.which("python")       if shutil.which("python")       is not None else "Cant find value"

sys.stdout.write(f"SystemRoot :            {path_SystemRoot}\n")
sys.stdout.write(f"PYTHONPATH:             {path_Python}\n")
sys.stdout.write(f"Python executable path: {python_exe_path}\n")

# At top of your application
from omni.isaac.kit import SimulationApp
config = {
     width: "1280",
     height: "720",
     headless: False,
}
simulation_app = SimulationApp(config)

# Rest of the code follows
...
simulation_app.close()