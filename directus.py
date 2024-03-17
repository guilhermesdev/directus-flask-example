import requests
import os

DIRECTUS_BASE_URL = os.environ.get("DIRECTUS_BASE_URL")


def get_global_data():
    response = requests.get(f"{DIRECTUS_BASE_URL}/items/global")
    return response.json().get("data")
