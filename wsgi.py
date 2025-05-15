import sys
import os

# Add the project directory to the Python path
project_home = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_home)

# Import the Flask app
from app import app as application

