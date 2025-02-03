class Local_LLama_Survey():

  def __init__(self):
    
    import ollama

    self.client = ollama.Client(host="http://127.0.0.1:11434")





  def answer(self, question, real_answer, answer, text):

    
    #pos

    response = self.client.chat (model='llama3.2:3b', messages=[
      {'role': 'system', 'content': "Sei l'assistente ad un sondaggio in lingua italiana, ad una persona saranno poste delle domande rigurdanti un testo. Tu dovrai controllare se sono giuste o no, e motivare brevemente il perchè secondo quel testo",
       'role': 'user', 'content': "La domanda posta dal sondaggio era la segurente:'"+ question+"', la risposta dell'utente è stata:'"+answer+"'e il testo su cui erano posto le damande era:'"+text+"'. Considerando che la risposta corretta è:'"+real_answer+"'', e motivarmi molto brevemente il perchè. Ricorda che la persona in question è un videoterminalista che deve seguire le istruzioni presenti nel documento. "}])


    if 'message' in response and 'content' in response['message']: 
      return response['message']['content'].strip()


    else:


      return "Non posso rispondere alla domanda."


