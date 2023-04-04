from flask import Flask,request
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_KEY')


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/chatgpt')
def chatgpt():
    args = request.args
    message =args.get("message")
    print(message)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return completion['choices'][0]['message']['content']

@app.route('/codegen')
def codegen():
    args = request.args
    language = args.get("language")
    content = args.get("content")
    parsed_content = urllib.parse.quote(content)
    prompt = f"Generate a {language} code snippet based on the following content:\n\n{content}\n\nCode:"
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return f"Generated {language} code snippet for:\n\n{content}\n\nCode:\n\n{completion.choices[0].text.strip()}"



