import sys
import os

# Add the current directory to path so Vercel can find app.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

# Vercel serverless handler
def handler(request):
    return app(request)