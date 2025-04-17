from requests import get
import os


def download_image(url, folder, file_name, api_key=""):
    os.makedirs(folder, exist_ok=True)
    full_path = os.path.join(folder, file_name)
    response = get(url, params=api_key)
    response.raise_for_status()
    with open(full_path, "wb") as file:
        file.write(response.content)
