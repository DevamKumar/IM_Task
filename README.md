The task is to develop a Python library that interacts with two different REST APIs:
Stripe API – to get the products and customers listed in the ui
restful-api.dev – A free dummy API service for testing GET/POST/PUT/DELETE operations.
The library will expose reusable functions that can be imported into any Python application.
A separate Python script will then import the library and display the response outputs from both APIs.

tasks:
1. Build a modular Python package that exposes clear API client functions.
2. Provide wrappers for calling Stripe and restful-api.dev endpoints.
3. Demonstrate usage via a separate sample script.

AssignmentTask/
|–  demo.py
|– stripe_client.py
|– restful_client.py
|- README.md


Python API Integration Library

Setup:
1. Install: pip3 install -r requirements.txt
2. Set STRIPE_API_KEY in environment or create a .env file with STRIPE_API_KEY=sk_test_...

Run demo:
python3 demo.py