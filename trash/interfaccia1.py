#Final app.py 
#import files
from flask import Flask, render_template, request
import openai
app = Flask(__name__)
openai.api_key  = "<place your openai_api_key>"

def get_completion():
   
    return "Ciao"


@app.route("/")
def home():    
    return render_template("chat1.html")
@app.route("/get")


def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText)  
    #return str(bot.get_response(userText)) 
    return response
if __name__ == "__main__":