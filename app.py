from flask import Flask
app = Flask(__name__)

@app.route('/')

def main():
  print ("Hay, loding from Python Codebase")
if __name__ == "__main__":
  app.run(host='0.0.0.')

   
