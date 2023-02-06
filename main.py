import typer
from revChatGPT import Official

def main(openai_api_key:str=""):
    if openai_api_key == "":
        raise ValueError("Need OPENAI_API_KEY - https://platform.openai.com/account/api-keys")

    print(f"Using OpenAI: {openai_api_key}")



if __name__ == '__main__':
    typer.run(main)

