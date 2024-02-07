import openai
openai.api_key="xxx"

test_key = "xxx"
model = "gpt-3.5-turbo"
messages = [
    {"role":"user","content":"请帮我写一句话，问候我"}
]

client = openai.OpenAI(api_key=test_key)
response = client.chat.completions.create(
    model = model,
    messages=messages
)

print(response.choice[0].message)
