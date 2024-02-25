import openai

openai.api_key = "sk-xxx"

completion = openai.ChatCompletion.create(
    model="ft:gpt-3.5-turbo-0613:personal::7qd0bfej",
    messages=[
        {"role": "system",
         "content": "Given a sports headline, provide the following fields in a JSON dict, where applicable: \"player\" (full name), \"team\", \"sport\", and \"gender\"."},
        {"role": "user", "content": "中北美杯-梅西世界波破门 迈阿密点球11-10夺冠"}
    ]
)

print(completion.choices[0].message)
