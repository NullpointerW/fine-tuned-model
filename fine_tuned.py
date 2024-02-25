import io
import json

import openai

openai.api_key = "sk-xxx"

#
# def tuned(data, id):
#     f = io.StringIO()
#     for qa in data:
#         print(qa)
#         prompt = {
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": qa.get("q")
#                 },
#                 {
#                     "role": "assistant",
#                     "content": qa.get("a")
#                 }
#             ]
#         }
#         json.dump(prompt, f)
#         f.write('\n')
#     print(f.getvalue())
#     f.seek(0)
#     resp = openai.File.create(
#         file=f,
#         purpose='fine-tune'
#     )
#     f.close()
#     print(resp)

#
# resp = openai.File.create(
#     file=open("wtf.jsonl", "rb"),
#     purpose='fine-tune'
# )
#
# template = '{"messages": [{"role": "user", "content": ""},{"role": "assistant", "content": ""}]}'
# print(resp)
# list = openai.File.list().data
# for i in list:
#     print(i)
# print(list)


# openai.FineTuningJob.create(training_file=resp.id, model="gpt-3.5-turbo")

resp = openai.FineTuningJob.list(limit=10)
print(resp)
