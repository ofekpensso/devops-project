from flask import Flask, render_template_string
import random

app = Flask(__name__)

quotes = [
    "It works on my machine.",
    "Premature optimization is the root of all evil.",
    "First, solve the problem. Then, write the code.",
    "Automation is cost-cutting by tightening the corners and not cutting them.",
    "Hardware eventually fails. Software eventually works."
]

@app.route('/')
def index():
    quote = random.choice(quotes)
    return render_template_string("""
        <html>
            <head>
                <title>DevOps Wisdom</title>
                <style>
                    body { font-family: 'Courier New', monospace; background-color: #282c34; color: #61dafb; text-align: center; padding-top: 50px; }
                    .container { border: 2px solid #61dafb; padding: 20px; display: inline-block; border-radius: 10px; }
                    h1 { color: #ffffff; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>DevOps Wisdom Generator</h1>
                    <h3>{{ quote }}</h3>
                </div>
            </body>
        </html>
    """, quote=quote)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
