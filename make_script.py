import ollama
from string import ascii_lowercase, ascii_letters
from random import randrange


def clean_message(content:str) -> str:
    return " ".join(content.split('\n'))


def get_random_prompt() -> str:
    prompt = get_llm_response("Return only the prompt and nothing else Write a good prompt for "
                              + "a youtube short and build it with the letters '" 
                              + ascii_lowercase[randrange(len(ascii_lowercase))] + "' and '" 
                              + ascii_lowercase[randrange(len(ascii_lowercase))] + "' in mind.")
    prompt.replace("\n", " ")
    return ''.join([char for char in prompt if char in (ascii_letters + ",.:?! <>_-1234567890")])


def get_llm_response(prompt:str, model:str="llama2") -> str:
    return ollama.generate(model=model, prompt=prompt)["response"]


def make_title(script:str, model:str="llama2") -> str:
    title_prompt = "Return only 1 title consisting of 25 characters or less and nothing else.\
          Return a super engaging and clickbait title for a youtube short based on the following script:\n"
    title = get_llm_response(title_prompt + script, model)
    title.replace("\n", " ")
    return ''.join([char for char in title if char in (ascii_letters + " -_1234567890")])
    


def make_script(prompt:str, model:str="llama2") -> str:
    print("Generating content...")
    content = get_llm_response(prompt, model)
    print("Content generated")
    print("Generating title...")
    title = make_title(content)
    print("Title generated")
    
    return title, clean_message(content)