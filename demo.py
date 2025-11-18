import os
import json
import restful_client
import stripe_client

def pretty_print(title: str, obj):
    print("\n-- {} --".format(title))
    try:
        print(json.dumps(obj, indent=2))
    except Exception:
        print(obj)
def run_demo():
    try:
        created_ids = []

        item1 = restful_client.create_item({"name": "Devam", "data": 111})
        pretty_print("Item created", item1)
        created_ids.append(item1.get("id") or item1.get("_id") or item1.get("object_id"))

        item2 = restful_client.create_item({"name": "Dileep", "data": 222})
        pretty_print("Item created", item2)
        created_ids.append(item2.get("id") or item2.get("_id") or item2.get("object_id"))

        item3 = restful_client.create_item({"name": "Rohan", "data": 333})
        pretty_print("Item created", item3)
        created_ids.append(item3.get("id") or item3.get("_id") or item3.get("object_id"))

        updated_item = restful_client.update_item(created_ids[1], {"name": "Dileep_Updated", "data": 999})
        pretty_print("Item updated", updated_item)

        fetched_item2 = restful_client.get_item(created_ids[1])
        pretty_print("Fetched Item 2", fetched_item2)

        fetched_items = [restful_client.get_item(i) for i in created_ids[0:3]]
        pretty_print("Fetched all items", fetched_items)

    except Exception as e:
        print(f"API failed: {e}")

# Stripe part
    try:
        products = stripe_client.get_products(limit=5)
        pretty_print("Stripe products", products)
        
        customers = stripe_client.get_customers(limit=5)
        pretty_print("Stripe customers", customers)

    except Exception as e:
        print("Stripe api failed: %s", e)

if __name__ == "__main__":
    run_demo()