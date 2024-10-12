# Reading PDF File
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter,CharacterTextSplitter,HTMLHeaderTextSplitter,RecursiveJsonSplitter

pdf_loader = PyPDFLoader('story.pdf')
pdf_document = pdf_loader.load()
# print(pdf_document)

# Recursive Text Splitter
text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50) # 500 characters overlap of 50 characters 
final_doc = text_splitter.split_documents(pdf_document)
# print(final_doc[0])


# Character Text Splitter
text_splitter=CharacterTextSplitter(separator="\n",chunk_size=500,chunk_overlap=50) # 500 characters overlap of 50 characters 
final_doc = text_splitter.split_documents(pdf_document)
# print(final_doc[0])
# print(final_doc[1])


#HTML Header Text Splitter
html_string = """
<!DOCTYPE html>
<html>
<body>
    <div>
        <h1>Foo</h1>
        <p>Some intro text about Foo.</p>
        <div>
            <h2>Bar main section</h2>
            <p>Some intro text about Bar.</p>
            <h3>Bar subsection 1</h3>
            <p>Some text about the first subtopic of Bar.</p>
            <h3>Bar subsection 2</h3>
            <p>Some text about the second subtopic of Bar.</p>
        </div>
        <div>
            <h2>Baz</h2>
            <p>Some text about Baz</p>
        </div>
        <br>
        <p>Some concluding text about Foo</p>
    </div>
</body>
</html>
"""

headers_to_split_on=[
    ("h1","Header 1"),
    ("h2","Header 2"),
    ("h3","Header 3"),
]
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on)
html_header_strings=html_splitter.split_text(html_string)
# print(html_header_strings)

#Recursive Json Splitter
import requests

json_data = requests.get("https://api.smith.langchain.com/openapi.json").json()
json_splitter = RecursiveJsonSplitter(max_chunk_size=300)
json_splitter_chunks=json_splitter.split_json(json_data)
for chunk in json_splitter_chunks[:3]:
    print(chunk)
