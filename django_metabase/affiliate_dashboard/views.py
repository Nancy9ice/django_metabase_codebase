from django.shortcuts import render
from django.http import HttpResponse
import jwt
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Metabase configuration using environment variables
METABASE_SITE_URL = os.getenv("METABASE_SITE_URL")
METABASE_SECRET_KEY = os.getenv("METABASE_SECRET_KEY")

# Helper function to generate JWT token
def get_token(payload):
    return jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

# Affiliate dashboard view
def affiliate_dashboard(request, affiliate_name):
    # Define payload for Metabase based on the affiliate_name
    payload = {
        "resource": {"dashboard": 2},  # Dashboard ID
        "params": {
            "affiliate": [affiliate_name]  # Pass the affiliate name to the dashboard
        }
    }
    iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + get_token(payload) + "#bordered=true&titled=true"

    # Render the dashboard with the correct iframe URL
    return render(request, 'affiliate_dashboard.html', {'iframeUrl': iframeUrl})