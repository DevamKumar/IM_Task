from dotenv import load_dotenv
import os
import requests

load_dotenv()

STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
BASE = "https://api.stripe.com/v1"

def _session():
    if not STRIPE_API_KEY:
        raise Exception("Missing STRIPE_API_KEY")
    s = requests.Session()
    s.auth = (STRIPE_API_KEY, "")
    return s

def get_products(limit=5):
    resp = _session().get(f"{BASE}/products", params={"limit": limit})
    if not resp.ok:
        raise Exception(resp.text)
    return resp.json()

def get_customers(limit=5):
    resp = _session().get(f"{BASE}/customers", params={"limit": limit})
    if not resp.ok:
        raise Exception(resp.text)
    return resp.json()