class Local_LLama():

  def __init__(self):
    
    import ollama

    self.client = ollama.Client(host="http://127.0.0.1:11434")





  def answer(self, question, text):



    response = self.client.chat (model='llama3.2:3b', messages=[
      {'role': 'system', 'content': 'Tu sei un assistente in lingua italiana che risponde a domande rigurdanti un documento',
      'role': 'user', 'content': "Considerato il documento: '"+text+"' rispondi alla domanda '"+question+"' .Rispondi unicamente con le informazioni presenti nel documento. Nel caso l'informazione non è presente rispondi con: 'Informazione non presente nel documento'"}
    ])


    if 'message' in response and 'content' in response['message']: 
      return response['message']['content'].strip()


    else:


      return "Non posso rispondere alla domanda."


