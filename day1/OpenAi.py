# 设置 API Key
import openai
openai.api_key = "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"

# 设置请求参数

model_engine = "text-davinci-002"

prompt = "python的应用领域"

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=3000,
    n=2,
    stop=None,
    temperature=0.5)

# 获取 ChatGPT 的回复
message = completions.choices[0].text

print(message)
