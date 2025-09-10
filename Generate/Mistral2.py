from huggingface_hub import InferenceClient
import random
from time import time as t
import os


class GenerateCode:
    def __init__(self, api_key_path="C:/J.A.R.V.I.S_A.I/api_key.txt"):
        self.API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
        self.api_key = self.load_api_key(api_key_path)
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

        self.messages = [
            {"role": "user", "content": "I'm jarvis AI Virtual Assistant, Developed by Haroon & Arbi"},
            {"role": "system", "content": "I am Jarvis, your AI Virtual Assistant, designed by Haroon Sajid and Adil Hayat. I'm here to assist you with various tasks and provide helpful information."},
            {"role": "user", "content": "Open Google Chrome."},
            {"role": "user", "content": "Summarize text"},
            {"role": "system", "content": "Python includes built-in functions you can use. For instance:"},
            {"role": "system", "content": "```python\n```"},
        ]

    def load_api_key(self, path):
        """Load API key from a local file."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"API key file not found at: {path}")
        with open(path, "r") as f:
            return f.read().strip()

    def format_prompt(self, message, custom_instructions=None):
        """Format prompt for the model."""
        prompt = ""
        if custom_instructions:
            prompt += f"[INST] {custom_instructions} [/INST]"
        prompt += f"[INST] {message} [/INST]"
        return prompt

    def Mistral7B(self, prompt, temperature=0.9, max_new_tokens=1024, top_p=0.95, repetition_penalty=1.0):
        """Generate a response using the Mistral-7B model."""
        start_time = t()

        # Ensure safe temperature values
        temperature = max(float(temperature), 1e-2)
        top_p = float(top_p)

        generate_kwargs = dict(
            temperature=temperature,
            max_new_tokens=max_new_tokens,
            top_p=top_p,
            repetition_penalty=repetition_penalty,
            do_sample=True,
            seed=random.randint(0, 10**7),
        )

        custom_instructions = str(self.messages)
        formatted_prompt = self.format_prompt(prompt, custom_instructions)

        self.messages.append({"role": "user", "content": prompt})

        # Hugging Face inference client
        client = InferenceClient(self.API_URL, headers=self.headers)
        response = client.text_generation(formatted_prompt, **generate_kwargs)

        self.messages.append({"role": "assistant", "content": response})

        print(f"Response time: {t()-start_time:.2f} seconds")
        return response


# Example usage:
# if __name__ == "__main__":
#     jarvis = GenerateCode(api_key_path="C:/J.A.R.V.I.S_A.I/api_key.txt")
#     user_input = "Who is the PM of Pakistan?"
#     response = jarvis.Mistral7B(user_input)
#     print(response)
