import ollama

def clean_message(content:str) -> str:
    return " ".join(content.split('\n'))

def random_prompt() -> str:
    return "Tell me about youtube, make it 5-7 sentences long"

def make_script(prompt:str, model:str="llama2") -> str:
    res = ollama.chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ])

    content = res["message"]["content"]
    title = "youtube short on youtube"

    return title, clean_message(content)