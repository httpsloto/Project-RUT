import openai
import subprocess
from colorama import Fore, Style
import pwinput
import json
import os


def askquestion(question, engine):
  completion = openai.Completion.create(
    engine=engine,
    prompt=question,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.5,
  )

  response = completion.choices[0].text
  return response


if __name__ == "__main__":
  print(Fore.GREEN + 'Made by @jacobpowaza on Replit \n' + Style.RESET_ALL)

  print(
    'I know, this is a turnoff but sadly, you cannot use ChatGPT without an API key.'
  )

  print(
    '\nWhy do I need this? We cannot use a private API key due to rate limits and privacy. You can find your api key at: '
    + Fore.BLUE + 'https://beta.openai.com/account/api-keys' + Style.RESET_ALL)

  print(
    '\nBut, there is a solution! If you go to this replit: ' + Fore.BLUE +
    'https://replit.com/@BenisBest/Firefox?v=1' + Style.RESET_ALL +
    ' and enter the link above, you can login to your account and find or create your API Key. For any issues you can check'
  )
  key = pwinput.pwinput(prompt='\nEnter API Key: ', mask='*')
  openai.api_key = key

  print("""
  GPT-3 Models:
  \tgpt-3.5-turbo (default, reccommended)
  \ttext-davinci-003
  \ttext-curie-001
  \ttext-babbage-001  
  \ttext-ada-001   
  \tgpt-4 (not widely available to public)
  """)
  model_engine = input('Select engine: ')
  if not model_engine:
    model_engine = 'gpt-3.5-turbo'

  print(
    Fore.GREEN +
    "Chat commands: \n\tExit - Straight forward. \n\tNano - To open the nano interface for longer messages"
    + Style.RESET_ALL)
  print("Hi, I'm a ChatGPT based AI. How can I help you today?")

  while True:
    question = input("You: ")

    if question.lower() == "exit":
      print("Bye! Have a great day.")
      break
    elif question.lower() == "nano":
      subprocess.call(['sh', './nano.sh'])

      print(
        Fore.GREEN +
        "\nTo use the text you just inputted, put [nano] somewhere in the text you're about to input. e.g 'Rewrite this email: [nano]' "
      )

      question = input("You: ")
      with open("./lines.txt", "r") as c:
        contents = c.read()
      question = question.replace('[nano]', contents)

    response = askquestion(question, model_engine)
    print("ChatGPT: " + response)