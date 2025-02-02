from flask import Flask, render_template,jsonify,request
from flask_cors import CORS
import requests,os
from dotenv.main import load_dotenv
from langchain.memory import ConversationSummaryBufferMemory
import torch


from Script.Structure.Document import Document
from Script.Model.BERTModel import BERT_Model
from Script.Pipeline.PipelineChat import Pipeline_Chatbot
from Script.Varius import util
from sentence_transformers import SentenceTransformer
from Script.Model.LLama_Local import Local_LLama
#from Script.Model.LLama_API import Local_LLama


#paraphrase-multilingual-mpnet-base-v2
#multi-qa-mpnet-base-dot-v1

model_doc=Document('Dataset/','Document.csv')
model_BERT=BERT_Model("paraphrase-multilingual-mpnet-base-v2", SentenceTransformer )
model_doc.load_document(0)

model_LLama=Local_LLama()

#memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():

    data = request.get_json()

    print(data)

    if data['mode']=="domande":

        return question(data)












def question(data):

    print("ciao")

    question=data.get('data')

    try:
        chatbot=Pipeline_Chatbot(model_BERT,question,model_doc.document_splitting('£'),model_doc.document_encoding(model_BERT),0)
        output = chatbot.pred_best_answer().replace("\n","")


        output=model_LLama.answer(question, output)


        print(output)


        #memory.save_context({"input": user_input}, {"output": output})
        return jsonify({"response":True,"message":output})

    except Exception as e:

        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message":error_message,"response":False})
        
if __name__ == '__main__':



    app.run()
