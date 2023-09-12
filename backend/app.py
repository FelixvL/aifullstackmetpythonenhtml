from flask import Flask
from flask_cors import CORS

import os
import openai

openai.api_key = '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'


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "wat is de hoofdstad van italie"
        }],
        temperature=0.5,
        max_tokens=256
    )
    #print(response)
    return response["choices"][0]["message"]["content"]