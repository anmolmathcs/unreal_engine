import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import openai
from config import OPENAI_API_KEY

def generate_script(prompt):
    """Generate a script using GPT-4 based on the given prompt."""
    client = openai.OpenAI(api_key=OPENAI_API_KEY)  # New way to initialize OpenAI client
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "Generate a monologue script."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # prompt = "Create a solo comedy skit where my character performs as if they are Donald Trump giving a speech at a completely unnecessary press conference. The speech should be full of exaggerated confidence, bizarre tangents, and classic Trump-style phrases like ‘many people are saying,’ ‘the best,’ and ‘tremendous.’ The character should react to imaginary reporters asking ridiculous questions, boast about their achievements (real or completely made up), and make wild promises like ‘I will personally negotiate with gravity to make people jump higher.’ Keep it lighthearted, humorous, and full of over-the-top Trumpisms!"
    prompt = "A very short humorous monologue inspired by Donald Trump"
    script = generate_script(prompt)
    print("\nGenerated Script:\n", script)