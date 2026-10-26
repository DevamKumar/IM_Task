import os
from dotenv import load_dotenv
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

# import stripe
# import os
# from dotenv import load_dotenv

# load_dotenv()  # Loads STRIPE_API_KEY from .env

# class StripeClient:
#     def __init__(self):
#         api_key = os.getenv("STRIPE_API_KEY")
#         if not api_key:
#             raise ValueError("STRIPE_API_KEY not found in environment variables")

#         stripe.api_key = api_key

#     def create_payment_intent(self, amount, currency="usd"):
#         return stripe.PaymentIntent.create(
#             amount=amount,
#             currency=currency
#         )