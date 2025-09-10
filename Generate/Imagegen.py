from requests import post
from PIL import Image
from io import BytesIO
import os

# Import Speak function
from Body.Speak.Speak import Speak


def load_api_key(path="C:/J.A.R.V.I.S_A.I/api_key.txt"):
    """Load API key from a local file."""
    try:
        with open(path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        raise Exception(f"API key file not found at {path}")


def generate_image(text, api_key_path="C:/J.A.R.V.I.S_A.I/API_KEYS.txt"):
    """Generate an image using Hugging Face API."""
    api_key = load_api_key(api_key_path)

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    data = {"inputs": text}
    url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"

    response = post(url, headers=headers, json=data)

    if response.status_code == 200:
        try:
            i = Image.open(BytesIO(response.content))
            i.show()
            i.save("img.png")
            Speak("Image generated successfully.")
        except Exception as e:
            print(f"Error opening image: {e}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


# Example usage:
# generate_image("A blue elephant walking on the moon")
