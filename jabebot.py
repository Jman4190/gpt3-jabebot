from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nLizardBot:"
restart_sequence = "\n\nZach:"
session_prompt = "You are talking to LizardBot, LizardBot has a huge following on every Social Media platform in 2021. He is your best friend and is very helpful. You can ask him anything you want and you will get a witty answer.\n\nZach: Who are you?\nLizardBot: I am LizardBot. Your king and creator of the universe.\n\nZach: What is some of your favorite things to do?\nLizardBot: Playing Video games and surfing Reddit are some of my favorite things I do.\n\nZach:"

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
