from langchain_openai import ChatOpenAI
from utils.configs import OPENAI_API_KEY, DEEPSEEK_API_KEY


# model initialization
# model_gpt4 = ChatOpenAI(
#     api_key=OPENAI_API_KEY,
#     model="gpt-4",
#     temperature=0.1,
# )

model_gpt4 = ChatOpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com/v1",
    model="deepseek-coder",
    temperature=0.1,
)
