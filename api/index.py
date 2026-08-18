"""
Vercel serverless entry point for the Gemati Flask application.
This file is required by Vercel to run the Flask app on their platform.
"""

import os
import sys
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Add parent directory to path so we can import app.py
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

try:
    from app import app
except ImportError as e:
    logging.error(f"Failed to import app from {ROOT}: {e}")
    raise

# Export for Vercel
application = app

# For local testing
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=False)
