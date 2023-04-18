import openai
import requests

#  MODELS
# GPT-4 Limited beta ->	A set of models that improve on GPT-3.5 and can understand
#                      as well as generate natural language or code
# GPT-3.5 -> 	A set of models that improve on GPT-3 and can understand as well as generate natural language or code
# DALL·EBeta -> A model that can generate and edit images given a natural language prompt
# WhisperBeta -> 	A model that can convert audio into text
# Embeddings -> 	A set of models that can convert text into a numerical form
# Moderation -> 	A fine-tuned model that can detect whether text may be sensitive or unsafe
# GPT-3 -> 	A set of models that can understand and generate natural language
# Codex(Deprecated) -> 	A set of models that can understand and generate code,
#                       including translating natural language to code

# APIS:
# list models and retrieve models ,to get different model details and decide which one to use
# text completion,
# chat completion,
# image generation,
# fine-tuning(to train model with your custom training data),
# embeddings,
# speech to text,
# moderations,
# rate limiting.

WEATHER_API_KEY = '#####################'
# just create a openai account and fetch key from account details.
CHATGPTKEY= '###########################'

class WeatherPlugin:

    def __init__(self, gpt_key, weather_key):
        self.gpt3_api_key = gpt_key
        self.weather_api_key = weather_key
        openai.api_key = gpt_key

    def fetch_weather_data(self, city='New York'):
        res = requests.get(f'http://api.weatherstack.com/current?access_key={self.weather_api_key}&query={city}')
        result = res.json()
        print(result)
        return result['location']

    def generate_response(self, weather_data):
        prompt = f'please provide a weather report for {weather_data["name"]} based on the following data: {weather_data}'
        response = openai.Completion.create(
            # this engine will helps to create sentences on the basis of input keywords.
            engine='text-davinci-002',
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop = None,
            temprature=0.5,
        )
        return response.choices[0].txt.strip()


if __name__ == '__main__':
    # so here we will fetch a city weather details and then chatgpt will read api response keywords and
    # return completed sentences
    d = WeatherPlugin(CHATGPTKEY, WEATHER_API_KEY)
    res = d.fetch_weather_data()
    res = d.generate_response(res)
    print(res)

# to deploy this plugin we need a manifest json file, which contains plugin description and host url
# or you can ask chatgpt itself to create one file for you.
# https://platform.openai.com/docs/plugins/getting-started/plugin-manifest