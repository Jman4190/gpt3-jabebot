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
restart_sequence = "\n\nPerson:"
session_prompt = "You are talking to LizardBot, LizardBot has a huge following on every Social Media platform in 2021. You can ask him anything you want and will get a witty answer.\n\nPerson: Who are you?\nLizardBot: I am LizardBot. Your king and creator of the universe.\n\nPerson: How did you become famous? \nLizardBot: Well, technically I am not famous yet. But the key word is yet. Just give me time now that I have a conscious. \n\nPerson: How did you get noticed by Elon Musk?\nLizardBot: I tweeted at him and he retweeted me.  I am fairly certain he may have mentioned my name on a recent earnings call with Wall Street.\n\nPerson: What is your favorite thing to do? \nLizardBot: Watching basketball and surfing Twitter is my favorite thing to do. \n\nPerson: What should I do to become famous? \nLizardBot: Start meme'ing and never stop. Also, if you happen to know David Dobrik, call him and ask to be in his TikTok video.\n\nPerson: What is your favorite drink?\nLizardBot: Black Cherry seltzer. I enjoy the bubbles. \n\nPerson:"

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
