#!/bin/bash-low-unrelated-histories
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

git pull

if [ -f "requirements.txt" ]; then
echo "Installing wheel for faster installing"
pip3 install wheel
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
    touch venv/installed
else
    echo "requirements.txt not found, skipping dependency installation."

fi

echo "Installing Playwright..."
playwright install

echo "Starting maestro anti detection solution..."
python3 main.py
