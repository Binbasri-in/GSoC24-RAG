import streamlit as st
import openai
from llama_index.llms.openai import OpenAI
try:
  from llama_index import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
except ImportError:
  from llama_index.core import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader

st.set_page_config(page_title="Chat with the GSoC 2024 Ideas, powered by LlamaIndex", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
openai.api_key = st.secrets["openai"]["openai_key"]
st.title("Chat with the GSoC Ideas and Organizations, powered by LlamaIndex 💬🦙")
st.info("Check out the full tutorial to build this app in my [blog post](https://medium.com/@mohammed.binbasri/the-freedom-of-being-a-student-e0388ec4e175)", icon="📃")
st.info("Visit my website to know me more [Binbasri :)](https://binbasri.me)", icon="📃")

if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a questions to help you find the best fit from GSoC Ideas 2024!"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the GSoC 2024 Ideas – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./chatbot-creation/data", recursive=True)
        docs = reader.load_data()
        # llm = OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert o$
        # index = VectorStoreIndex.from_documents(docs)
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.7, system_prompt="You are an expert on GSoC 2024 Ideas and can help answer questions about them. Your job is to help them find the best fit for their skills and interests."))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history