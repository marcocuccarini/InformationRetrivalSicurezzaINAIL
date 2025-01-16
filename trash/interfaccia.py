from flask import Flask, render_template, request, jsonify
import torch

from Script.Structure.Document import Document
from Script.Model.BERTModel import BERT_Model
from Script.Pipeline.PipelineChat import Pipeline_Chatbot
from Script.Varius import util
from sentence_transformers import SentenceTransformer



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)


def get_Chat_response(text):


    print("ciao")

    model_doc=Document('Dataset/','Rule_Hotel_Hand.csv')
    model_BERT=BERT_Model("multi-qa-mpnet-base-dot-v1", SentenceTransformer )
    model_doc.load_document(1)



    chatbot=Pipeline_Chatbot(model_BERT,text,model_doc.document_splitting('£'),model_doc.document_encoding(model_BERT),1)


    return chatbot.pred_best_answer().replace("\n","")
     
    # Let's chat for 5 lines
    


if __name__ == '__main__':
    app.run()
