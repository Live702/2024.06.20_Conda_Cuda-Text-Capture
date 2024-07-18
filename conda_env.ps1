# Check Conda installation path
Write-Output "Checking Conda installation path..."
$where_conda = where conda
if (-not $where_conda) {
    Write-Output "Conda is not in PATH. Please add it to your PATH."
} else {
    Write-Output "Conda found at: $where_conda"
}

# Initialize Conda for all shells
Write-Output "Initializing Conda for all shells..."
conda init --all

# Test manual activation
Write-Output "Testing manual activation..."
& "C:\Users\Conda\Anaconda3\Scripts\activate" pytorch_env

# Add to PowerShell profile if manual activation works
if ($?) {
    Write-Output "Manual activation succeeded. Updating PowerShell profile..."
    if (-not (Test-Path $PROFILE)) {
        New-Item -Path $PROFILE -Type File -Force
    }
    Add-Content -Path $PROFILE -Value '& "C:\Users\Conda\Anaconda3\condabin\conda-hook.ps1"'
    Write-Output "Profile updated. Please restart Visual Studio Code."
} else {
    Write-Output "Manual activation failed. Please check your Conda installation."
}