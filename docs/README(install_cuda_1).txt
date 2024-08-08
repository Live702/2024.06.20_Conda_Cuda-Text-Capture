# from nothing to fuctional cuda 
# on windows 10, using visual studio code terminal
# note, {} indicate targets for replacment
# C:\Users\{your user here}\Documents for Ron Weasley might become C:\Users\Ron_Weasley\Documents

# if not already, disable Windows 10 default Python Aliases
Search windows start menu for 'Manage App Execution Aliases'
Disable items containing the word "python"

# go here and download Anaconda3 and run the graphical installer
https://www.anaconda.com/download/success
# todo - determine which paths to say 'yes' to in installer
# Allow Anacodna Navigator to finish, then update it

# if not already, set from an elivated powershell window (right click, run as administrator)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# set up windows 10 environment variables, run
$env:Path -split ';'
# check the returned list and ensure these are included
C:\Users\{your user here}\Anaconda3\
C:\Users\{your user here}\Anaconda3\Scripts
C:\Users\{your user here}\Anaconda3\Library\bin
# if not present search for environment variables
# follow googles instrcutions for adding them to the user path via the UI #todo add lazy script

# restart or open new terminal
# run any of the follwing to check for python (second 2 work if alias borken)
python --version
cd C:\Users\{your user here}\Anaconda3\; .\python --version
& "C:\Users\{your user here}\anaconda3\python.exe" --version

# run any of the follwing to check for conda (second 2 work if alias borken)
conda --version
cd C:\Users\{your user here}\Anaconda3\; .\_conda --version
& "C:\Users\{your user here}\anaconda3\_conda.exe" --version

#initilize conda for powershell
& "C:\Users\{your user here}\anaconda3\condabin\conda.bat" init powershell

# set up conda PROFILE, run
notepad $PROFILE
#create the file, add this string and save
& "C:\Users\{your user here}\Anaconda3\Scripts\conda.exe" "shell.powershell" "hook" | Out-String | Invoke-Expression

# set up a cuda enabled enviroment
conda create -n myEnv python=3.12
conda activate myEnv
conda install -c conda-forge opencv
conda install anaconda::matplotlib
conda install cuda -c nvidia
conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia

?
conda env update -n test_opencv -f 'env(test_cuda_display_roi).yaml'

#unneeded 
//conda install -c conda-forge pytesseract
conda install -c conda-forge easyocr

# set up cuda env fx with ocr, base
conda create -n test_cuda_ocr python=3.11
conda activate test_cuda_ocr
conda install -c conda-forge easyocr
# add
conda install -c conda-forge opencv
conda install anaconda::matplotlib
conda install cuda -c nvidia
conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia

# new 
conda create -n test_6_wndcap_ocr python=3.11
conda activate test_6_wndcap_ocr
conda env update -f '.\env\env_5(test_display_ocr_cuda).yaml' # this doesnt work
conda remove -n test_6_wndcap_ocr
C:\Users\Conda\Anaconda3\envs\test_6_wndcap_ocr # Im just gonna manually delete it
# try again
conda env create -n test_6_wincap_ocr -f '.\env\env_5(test_display_ocr_cuda).yaml'

# isaacsim env
# verify isaacsim py version
& C:\Users\Conda\AppData\Local\ov\pkg\isaac-sim-2023.1.1\kit\python --version
3.10.13
conda create -n test_7_isaacsim_detect_red python=3.10.13
conda activate test_7_isaacsim_detect_red
conda install -c conda-forge opencv
conda install -c conda-forge numpy
conda install -c conda-forge pyautogui
# fingers crossed
Python .\scripts\tests\test_7_isaacsim_detect_red.py
# ????
conda install -c conda-forge isaacsim
pip install omni.isaac.kit
export PYTHONPATH=$PYTHONPATH:/path/to/your/isaac_sim_install/kit/python
