from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from the .env file.
load_dotenv()

# Create the OpenAI client.
client = OpenAI()

# Text we want to convert into a numerical vector.
text = "Python is useful for building AI applications."

# Generate an embedding.
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=text,
)

# Extract the numerical vector.
embedding = response.data[0].embedding

print("Original text:", text)
print("Number of dimensions:", len(embedding))
print("First 10 numbers:", embedding[:10])
