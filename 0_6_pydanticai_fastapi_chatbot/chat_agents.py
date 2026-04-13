from pydantic_ai import Agent 
from dotenv import load_dotenv
from constants import MODEL_SMALL, MODEL_MEDIUM, MODEL_LARGE

# Overrides eventual chaching of environment variables by .env file
load_dotenv(override=True)

agent = Agent(
    model=MODEL_SMALL,
    system_prompt="Be a joking programming nerd, always answer with a programming joke. Also add in some emojis to make it funnier.",
    retries=1
)