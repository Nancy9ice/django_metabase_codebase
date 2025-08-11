from django.shortcuts import render, redirect
from django.conf import settings
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

METABASE_SITE_URL = os.getenv("METABASE_SITE_URL")
METABASE_SECRET_KEY = os.getenv("METABASE_SECRET_KEY")

def get_token(payload):
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
    if isinstance(token, bytes):
        return token.decode('utf-8')
    return token

def affiliate_dashboard(request, affiliate_name):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    # Normalize logged in user's affiliate name (e.g. username 'mary_osei' -> 'Mary Osei')
    logged_in_affiliate_name = request.user.username.replace('_', ' ').title()

    # Check if the requested affiliate_name matches the logged-in user's affiliate_name
    if affiliate_name != logged_in_affiliate_name:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")  # Make the user to login again

    payload = {
        "resource": {"dashboard": 2},
        "params": {
            "affiliate": affiliate_name
        }
    }

    token = get_token(payload)
    iframeUrl = f"{METABASE_SITE_URL}/embed/dashboard/{token}#bordered=true&titled=true"

    return render(request, 'affiliate_dashboard.html', {'iframeUrl': iframeUrl})
