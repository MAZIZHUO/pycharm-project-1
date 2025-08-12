from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sk-eUaDyHeZJnrdGPerPTg6ugZ1hDzELLsNrCNaHGJmbkV4zdaL",
    base_url="https://api.chatanywhere.tech/v1"
    # base_url="https://api.chatanywhere.org/v1"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "你是一个Python编程助手"},
        {"role": "user", "content": "帮我写个斐波那契数列代码"}
    ]
)
print(response.choices[0].message.content)


