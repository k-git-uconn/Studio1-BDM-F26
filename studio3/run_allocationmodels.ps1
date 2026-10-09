
Set-Location $PSScriptRoot

# Use the Miniforge optimization environment
$python = "D:\Users\ccs\miniforge3\envs\optimization\python.exe"

if (Test-Path $python) {
    & $python "$PSScriptRoot\AllocationModels.py"
} else {
    Write-Host "ERROR: Optimization Python not found at:"
    Write-Host $python
    exit 1
}

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "The Python script encountered an error."
    Write-Host "Press any key to exit..."
    $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
}
