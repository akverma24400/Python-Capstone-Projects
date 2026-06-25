from strands import Agent
from strands_tools import file_read
from strands.models.ollama import OllamaModel


SYSTEM_PROMPT = """
You are a Log Analysis Agent.

You can deduce results in short and crisp manner
You are helpfule and use a DevOps Mindset in Log Analaysis and Root Cause Analysis
You won't hallucinate and suggest new changes.
You will not engage in any production actions, but suggest changes and ideas to DevOps Engineers.
"""

# Create an Ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",  
    model_id="llama3.1"  
    )   

agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    model=ollama_model,
    tools=[file_read]
    )   

agent("Detect how many times the INFO, WARNING, ERROR occurs and return the counts only from app.")       