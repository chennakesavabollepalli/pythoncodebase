from flask import Flask
app = Flask(__name__)
visitCount = 0

@app.route('/')

def main():
  global visitCount
  visitCount+=1
  return "Hay, loading from Python Codebase!" + str(visitCount)
if __name__ == "__main__":
  app.run(host='0.0.0.', debug=True)

   
