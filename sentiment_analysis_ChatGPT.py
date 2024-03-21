import openai

# OpenAI API key
openai.api_key = 'xxx'
import openai
import re  


# Define the client
client = openai.OpenAI(api_key=openai.api_key)


def analyze_sentiment(sentence):
    prompt = f"Please analyze the sentiment of the following Portuguese sentence and provide a numerical sentiment score from -1 (very negative) to +1 (very positive):\n\nSentence: \"{sentence}\""

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-3.5-turbo"
        )
        response_text = response.choices[0].message.content.strip()
        # Extracting the numerical part from the response using regular expression
        match = re.search(r"[-+]?\d*\.\d+|\d+", response_text)
        if match:
            return float(match.group())
        else:
            print("No numerical sentiment score found in the response.")
            return None
    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        return None


# Portuguese sentences for sentiment analysis
sentences = [
    "desemprego tem vindo registar nívei histórico preocupante futuro do país, tendo atingido 11,2%, dado oficiais, ultrapassando 600 mil desempregado inscrito centro emprego significar desemprego real acima.",
    "criar condições apoio às vítimas, sejar ao nível judicial, sejar ao nível laboral, dar prioridade à sua integração empregabilidade em caso necessária deslocação sua área residência; garantir educação formação do individuo, protegendo promovendo escola público acesso gratuito nívei ensino, articulado com as necessidad desenvolvimento do país, promovendo as saída profissionais defendendo direito professor, em articulação com sector."
]

# Analyze sentiment for each sentence
for sentence in sentences:
    sentiment_score = analyze_sentiment(sentence)
    print(f"Sentence: {sentence}\nSentiment Score: {sentiment_score}\n")
