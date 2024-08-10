"""
Lack of conda support makes this hard to store env. 
These are the commands I used to create this env

conda create -n test_8_isaacsim_env python=3.10
conda activate test_8_isaacsim_env
pip install --upgrade pip
pip install isaacsim==4.1.0.0 --extra-index-url https://pypi.nvidia.com
pip show isaacsim
python -c "import isaacsim"
"""

from isaacsim import SimulationApp

config = {
    "width": "1280",
    "height": "720",
    "headless": False,
}

simulation_app = SimulationApp(config)
simulation_app.close()

