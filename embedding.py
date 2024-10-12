import os
from dotenv import load_dotenv
load_dotenv() 

os.environ["OPENAI_API_KEY"]= os.getenv("OPENAI_API_KEY")
from langchain_openai import OpenAIEmbeddings
embeddings=OpenAIEmbeddings(model="text-embedding-3-small")
embeddings

text="This is a tutorial on OPENAI embedding"
query_result=embeddings.embed_query(text)
print(query_result)
print(query_result[0])
print(len(query_result))
