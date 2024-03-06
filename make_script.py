import ollama

def clean_message(content:str) -> str:
    return " ".join(content.split('\n'))

def get_random_prompt() -> str:
    prompt = "Say only the riddle and the solution. Do not say 'ok' or any other acknowledgement. Give me a riddle that is 5-7 sentences long, then say the solution."
    return prompt

def make_script(prompt:str, model:str="llama2") -> str:
    res = ollama.chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ])

    content = res["message"]["content"]
    title = "Daily brain teaser"

    return title, clean_message(content)