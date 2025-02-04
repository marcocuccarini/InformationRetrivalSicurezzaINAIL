class Local_LLama_Survey():

  def __init__(self):
    
    import ollama

    self.client = ollama.Client(host="http://127.0.0.1:11434")





  def answer(self, question, real_answer, answer, text):

    
    #pos

    response = self.client.chat (model='deepseek-r1:7b', messages=[
      {'role': 'system', 'content': "Tu sei l'assistente in lingua italiana",
       'role': 'user', 'content': "La domanda: '"+question+"'  ha come risposta GIUSTA:'"+real_answer+"''. L'utente ha risposto in maniera errata:'"+answer+"'. Scrivi se l'utente ha rispsoto bene e la sua motivazione usando le informazioni presenti in:'"+text+"''. Scrivi al massimo tre righe di risposta."}])


    if 'message' in response and 'content' in response['message']: 
      return response['message']['content'].strip()


    else:


      return "Non posso rispondere alla domanda."


