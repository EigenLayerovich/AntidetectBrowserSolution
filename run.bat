@echo off

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

git pull

echo Activating virtual environment...
call venv\Scripts\activate

if exist requirements.txt (
    echo installing wheel for faster installing
    pip install wheel
    echo Installing dependencies...
    pip install -r requirements.txt
    echo. > venv\Lib\site-packages\installed
) else (
    echo requirements.txt not found, skipping dependency installation.
)

echo Installing Playwright...
playwright install

echo Starting maestro anti detection solution...
python main.py

pause