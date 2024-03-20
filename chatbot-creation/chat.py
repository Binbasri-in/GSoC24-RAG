# Option 3:
import pandas as pd
from llama_index.core import Document
from llama_index.core import get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.agent.openai import OpenAIAgent

import os

os.environ["OPENAI_API_KEY"] = "<your-openai-api-key>"

combined_df = pd.read_csv('./data/ideas_data.csv')

# Create a list of Document objects out of each row in the DataFrame
documents = []
for index, row in combined_df.iterrows():
    details = f"Title: {row['idea title']}\nDescription: {row['idea description']}\nSkills: {row['skills']}\nDuration: {row['duration']}\nDifficulty: {row['difficulty']}"
    doc = Document(
        text=details,
        metadata={
            
            'organization': row['organization'],
            'ideas_link': row['ideas_link']
        }
    )
    documents.append(doc)
    

# configure retriever
retriever = VectorIndexRetriever(
    index=index,
    similarity_top_k=10,
)

# configure response synthesizer
response_synthesizer = get_response_synthesizer()

# assemble query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
    node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.6)],
)



query_engine_tool = QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="gsoc_ideas",
            description=(
                "Provides information about Google Summer of Code project ideas."
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),

agent = OpenAIAgent.from_tools(query_engine_tool, verbose=True)

agent.chat_repl()