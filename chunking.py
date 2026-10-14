import re

CHUNK_SIZE = 15
CHUNK_OVERLAP = 5


def create_chunks(text: str) -> list[str]:
    """Split text into word-limited chunks with word-based overlap."""

    # Step 1: Split text into sentences.
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    # Step 2: Split oversized sentences into smaller pieces.
    processed_sentences = []

    for sentence in sentences:
        words = sentence.split()

        if len(words) > CHUNK_SIZE:
            for i in range(0, len(words), CHUNK_SIZE):
                piece = " ".join(words[i : i + CHUNK_SIZE])
                processed_sentences.append(piece)
        else:
            processed_sentences.append(sentence)

    # Step 3: Combine the processed sentences into one word list.
    words = " ".join(processed_sentences).split()

    # Step 4: Create chunks with word-based overlap.
    chunks = []
    step = CHUNK_SIZE - CHUNK_OVERLAP

    for i in range(0, len(words), step):
        chunk_words = words[i : i + CHUNK_SIZE]
        chunks.append(" ".join(chunk_words))

    return chunks


text = """
Python is easy to learn. Python is useful for building AI applications.
Artificial intelligence allows computers to perform tasks that usually require human intelligence and reasoning in many different real-world situations across various industries today.
"""

print(create_chunks(text))
