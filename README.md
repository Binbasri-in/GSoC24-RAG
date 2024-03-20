[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/H2H5VAL6E)

# 🦙📚 GSoC24-RAG

A simple chatbot that is RAG with GSoC projects and ideas.

Check out the deployed version: [Start Chat](#)

## Installation
```bash
pip install -r requirements.txt
```


### create the RAG CLI

```bash
export OPENAI_API_KEY=<api_key>

llamaindex-cli rag --files "./chatbot-creation/data"

llamaindex-cli rag --question "give me list of 10 easy ideas with python and Machine Learning?"

llamaindex-cli rag --chat
```

### Create the full stack chatbot

for this to work you need to have these stuff installed [npm](https://www.npmjs.com/get-npm), [node](https://nodejs.org/en/download/), [pipx](https://pypa.github.io/pipx/), [poetry](https://python-poetry.org/docs/), [llamaIndex-cli](https://docs.llamaindex.ai/en/stable/use_cases/q_and_a/rag_cli.html)


```bash
llamaindex-cli rag --create-llama
```

### To run chat in command line with my code

```bash
cd chatbot-creation
python chat.py
```


## Development plan

- [x] Data collection and extraction, check [data-collection](./data-collection)
- [x] Data Loading and Ingestion Pipeline [chatbot-creation](./chatbot-creation)
- [ ] Chatbot deployment


## Check out the following resources for more information

- [LlamaIndex](https://docs.llamaindex.ai/en/stable/index.html)
- [Haystack](https://docs.haystack.deepset.ai/docs/intro)
- [spaCy](https://spacy.io/usage/large-language-models)
- [Google AI Studio](https://aistudio.google.com/)
- [OpenAI](https://platform.openai.com/)

## Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.