import ollama

def clean_message(content:str) -> str:
    return " ".join(content.split('\n'))

def get_random_prompt() -> str:
    prompt = "Give me a daily fitness tip about discipline and success, make it 5-7 sentences long"
    return prompt

def make_script(prompt:str, model:str="llama2") -> str:
    res = ollama.chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ])

    content = res["message"]["content"]
    title = "Fitness tip of the Day"

    return title, clean_message(content)