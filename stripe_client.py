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

def create_checkout_session():
    data = {
        "success_url": "https://example.com/success",
        "cancel_url": "https://example.com/cancel",
        "mode": "payment",
        "line_items[0][price_data][currency]": "usd",
        "line_items[0][price_data][product_data][name]": "Test_item_devam",
        "line_items[0][price_data][unit_amount]": 100,
        "line_items[0][quantity]": 20,
    }

    resp = _session().post(f"{BASE}/checkout/sessions", data=data)
    if not resp.ok:
        raise Exception(resp.text)
    return resp.json()
