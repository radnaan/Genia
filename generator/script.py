# Generate a new title and script using GPT-3
prompt = 'Generate a video title and script based on the trending topics on Reddit and YouTube.'

model = 'text-davinci-002'
temperature = 0.5
max_tokens = 1024

response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    n=1,
    stop=None,
    timeout=60,
)

title = response.choices[0].text.strip()
script = response.choices[0].text.strip()

print('Generated title:', title)
print('Generated script:', script)
