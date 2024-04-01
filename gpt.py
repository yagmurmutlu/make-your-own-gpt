import openai
import time

# Gizli anahtarınızı buraya ekleyin
#https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key--
#BU SAYFAYA GİDEREK APİ KEY'İNİZİ ALABİLİRSİNİZ
openai.api_key = ""

def ask_openai(prompt):
    model_engine = "gpt-3.5-turbo" #ücretsiz en son sürüm 
    
    try:
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None
        )
        
        return response.choices[0].text
    except openai.error.RateLimitError:
        print("Cevap için biraz bekle")
        time.sleep(60)  # 60 saniye bekleyin
        return ask_openai(prompt)

while True:
    prompt = input("Konuşmayı başlat: ")
    
    if 'exit' in prompt or 'quit' in prompt:
        break
    
    response_text = ask_openai(prompt)
    print(response_text)
