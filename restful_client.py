import requests
from typing import Dict, Any

BASE_URL = "https://api.restful-api.dev/objects"

def get_item(obj_id: str) -> Dict[str, Any]:
    resp = requests.get(f"{BASE_URL}/{obj_id}")
    if not resp.ok:
        raise Exception(f"error: {resp.status_code}, {resp.text}")
    return resp.json()

def create_item(data: Dict[str, Any]) -> Dict[str, Any]:
    resp = requests.post(BASE_URL, json=data)
    if not resp.ok:
        raise Exception(f"error: {resp.status_code}, {resp.text}")
    return resp.json()

def update_item(obj_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    resp = requests.put(f"{BASE_URL}/{obj_id}", json=data)
    if not resp.ok:
        raise Exception(f"error: {resp.status_code}, {resp.text}")
    return resp.json()

def delete_item(obj_id: str) -> Dict[str, Any]:
    resp = requests.delete(f"{BASE_URL}/{obj_id}")
    if not resp.ok:
        raise Exception(f"error: {resp.status_code}, {resp.text}")
    return resp.json()