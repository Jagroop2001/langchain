# Text Loaders
from langchain_community.document_loaders import TextLoader

loader = TextLoader('speech.txt')
text_documents = loader.load()
# print(text_documents)


# Reading PDF File
from langchain_community.document_loaders import PyPDFLoader
pdf_loader = PyPDFLoader('speech.pdf')
pdf_document = pdf_loader.load()
# print(pdf_document)

# Web based loader
from langchain_community.document_loaders import WebBaseLoader
import bs4
import os

os.environ['USER_AGENT'] = 'MyApp/1.0 (https://example.com)'

# Load the document from the web
web_loader = WebBaseLoader(
    web_paths=("https://chatgpt.com/share/670a606e-8bac-800f-90c7-91bcb8df2cea",),
    bs_kwargs=dict(parse_only=bs4.SoupStrainer('p'))
)

web_doc = web_loader.load()
# print(web_doc)


# Arxiv
from langchain_community.document_loaders import ArxivLoader
docs = ArxivLoader(query="1706.03762",load_max_docs=2).load()
print(docs)