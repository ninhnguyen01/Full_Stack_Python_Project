from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
  <body>
    <h1>Flask Example</h1>
    <h2>Say hello to my little friend!</h2>
  </body>
</html>
'''

app.run(port=9999)
