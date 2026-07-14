
cd src
python3 -m venv .venv
echo "virtual Environment created"
.venv/*/pip install .
echo "dependencies installed"
echo "running main.py ..."
.venv/*/python ../main.py
