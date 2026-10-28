$ErrorActionPreference = 'Stop'
# Run this script from the extracted project directory. It avoids PowerShell activation-policy issues.
if (!(Test-Path '.\myenv\Scripts\python.exe')) {
    if (Get-Command 'py' -ErrorAction SilentlyContinue) {
        try { py -3.11 -m venv myenv }
        catch { python -m venv myenv }
    } else {
        python -m venv myenv
    }
}
$venvPython = '.\myenv\Scripts\python.exe'
& $venvPython -m pip install --upgrade pip
& $venvPython -m pip install -r requirements.txt
& $venvPython app.py
