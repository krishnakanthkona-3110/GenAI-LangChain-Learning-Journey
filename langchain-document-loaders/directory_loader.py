from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = 'Langchain-document-loaders/Books',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

docs = loader.load()
#docs = loader.lazy_load()

for document in docs:
    print(document.metadata)


