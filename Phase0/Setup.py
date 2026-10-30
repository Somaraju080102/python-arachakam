mkdir py-practice && cd py-practice
python -m venv .venv

# activate it
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate           # Windows

# you'll see (.venv) in your prompt now
pip install requests
pip list
pip freeze > requirements.txt    # like a pom.xml, a snapshot of your deps
deactivate                       # leave the toolbox