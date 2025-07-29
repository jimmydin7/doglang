from flask import Flask, render_template_string, request
import io
import sys
from lang.tokenizer.lexer import Tokenizer
from lang.parser.parser import Parser
from lang.interpreter.interpreter import Interpreter

app = Flask(__name__)

DOG_LANG_DOCS = '''
<h3>Doglang Quick Docs 🐶</h3>
<ul>
  <li><b>Say something:</b> <code>barg("Hello!")</code></li>
  <li><b>Variables:</b> <code>sniff x = int(5)</code></li>
  <li><b>Repeat:</b> <code>zoomies 3 { barg("Woof!") }</code></li>
  <li><b>Condition:</b> <code>goodboy x = 5 { barg("Good boy!") }</code></li>
  <li><b>Functions:</b> <code>doggo greet { barg("Hi!") } bark greet</code></li>
</ul>
<pre>
# Example:
sniff x = int(2)
zoomies 3 {
  barg("Woof!")
  sniff x = int(x + 1)
}
</pre>
'''

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Doglang</title>
  <style>
    body { font-family: sans-serif; background: #f9f9f9; margin: 0; padding: 0; }
    .container { max-width: 800px; margin: 40px auto; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px #0001; padding: 32px; }
    textarea { width: 100%; height: 180px; font-family: monospace; font-size: 1.1em; border-radius: 4px; border: 1px solid #ccc; padding: 8px; }
    .output { background: #222; color: #0f0; padding: 16px; border-radius: 4px; min-height: 60px; margin-top: 16px; font-family: monospace; }
    .docs { background: #f0f0f0; border-radius: 4px; padding: 16px; margin-bottom: 24px; }
    button { background: #ff9800; color: #fff; border: none; border-radius: 4px; padding: 10px 24px; font-size: 1.1em; cursor: pointer; }
    button:hover { background: #e65100; }
    h1 { margin-top: 0; }
  </style>
</head>
<body>
  <div class="container">
    <h1>Doglang Web Playground 🐶</h1>
    <h2>Made with love by Jim for twist</h2>
    <div class="docs">{{ docs|safe }}</div>
    <form method="post">
      <textarea name="code" required>{{ code }}</textarea><br>
      <button type="submit">Run</button>
    </form>
    <h3>Output:</h3>
    <div class="output">{{ output }}</div>
  </div>
</body>
</html>
'''

def run_doglang_code(source_code):
    try:
        lexer = Tokenizer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)

        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            interpreter.run()
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        return output or '(no output)'
    except Exception as e:
        return f'Error: {e}'

@app.route('/', methods=['GET', 'POST'])
def index():
    code = request.form.get('code', 'barg("Hello from Doglang!")')
    output = ''
    if request.method == 'POST':
        output = run_doglang_code(code)
    return render_template_string(HTML_TEMPLATE, code=code, output=output, docs=DOG_LANG_DOCS)

if __name__ == '__main__':
    app.run(debug=True) 