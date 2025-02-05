from flask import Flask, render_template,jsonify,request
from flask_cors import CORS
import requests,os
from dotenv.main import load_dotenv
from langchain.memory import ConversationSummaryBufferMemory
import torch
from data import dataset_QA_survey, dataset_QA_survey_short

from Script.Structure.Document import Document
from Script.Model.BERTModel import BERT_Model
from Script.Pipeline.PipelineChat import Pipeline_Chatbot
from Script.Varius import util
from sentence_transformers import SentenceTransformer
from Script.Model.LLama_Local import Local_LLama
from Script.Model.LLama_Local_Survey import Local_LLama_Survey

#from Script.Model.LLama_API import Local_LLama


#paraphrase-multilingual-mpnet-base-v2
#multi-qa-mpnet-base-dot-v1

model_doc=Document('Dataset/','Document.csv')
model_BERT=BERT_Model("paraphrase-multilingual-mpnet-base-v2", SentenceTransformer )
model_doc.load_document(0)
model_LLama=Local_LLama()
model_LLama_Survey=Local_LLama_Survey()

#memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():

    data = request.get_json()

    if data['mode']=="domande":

        return question(data)

    else: 

        return survey(data)


def survey(data):

    answer=data.get('data')
    index=data.get('cont')
    try:
        chatbot1=Pipeline_Chatbot(model_BERT,dataset_QA_survey_short[index][0],model_doc.document_splitting('£'),model_doc.document_encoding(model_BERT),0)
        output1 = chatbot1.pred_best_answer().replace("\n","")
        output=model_LLama_Survey.answer(dataset_QA_survey_short[index][0], dataset_QA_survey_short[index][1], answer, dataset_QA_survey_short[index][2])

        #memory.save_context({"input": user_input}, {"output": output})
        return jsonify({"response":True,"message":output,"nextquestion": dataset_QA_survey_short[index+1][0]})

    except Exception as e:

        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message":error_message,"response":False})

def question(data):


    question=data.get('data')

    try:
        chatbot=Pipeline_Chatbot(model_BERT,question,model_doc.document_splitting('£'),model_doc.document_encoding(model_BERT),0)
        output = chatbot.pred_best_answer().replace("\n","")
        output=model_LLama.answer(question, output)

        #memory.save_context({"input": user_input}, {"output": output})
        return jsonify({"response":True,"message":output, "nextquestion": "Posso esserti utile in qualche altro modo?"})

    except Exception as e:

        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message":error_message,"response":False, "nextquestion":False})
        
if __name__ == '__main__':



    app.run()
