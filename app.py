from flask import Flask
from redis import Redis

app = Flask(__name__)
redisDB = Redis(host=os.getenv('RedisHOST'), port=os.getenv('RedisPORT'))
visitCount = 0

@app.route('/')

def main():
  #global visitCount
  #visitCount+=1
  redisDB.incr('visitorCount')
  visitCount = str(redisDB.get('visitorCount'),'utf-8')
  return "Hay, loading from Python Codebase!" + str(visitCount)
if __name__ == "__main__":
  app.run(host='0.0.0.', debug=True)

   
