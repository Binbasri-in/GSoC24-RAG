# GSoC24-RAG
A simple chatbot that is RAG with GSoC projects

## Installation
```bash
pip install -r requirements.txt
```


## create the RAG CLI

```bash
export OPENAI_API_KEY=<api_key>
llamaindex-cli rag --files "./chatbot-creation/data"

llamaindex-cli rag --question "give me list of 10 easy ideas with python and Machine Learning?"

llamaindex-cli rag --chat
```

## Create the full stack chatbot

for this to work you need to have these stuff installed [npm](https://www.npmjs.com/get-npm), [node](https://nodejs.org/en/download/), [pipx](https://pypa.github.io/pipx/), [poetry](https://python-poetry.org/docs/), [llamaIndex-cli](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/rag_cli.html)


```bash
llamaindex-cli rag --create-llama
```
