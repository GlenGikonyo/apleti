import sys
import os

# Add the project directory to the Python path
project_home = '/home/ypokghte/public_html/apleti'
sys.path.insert(0, project_home)

# Import the Flask app
from app import app as application