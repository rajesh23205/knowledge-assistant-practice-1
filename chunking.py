import re

CHUNK_SIZE = 15
CHUNK_OVERLAP = 5


def create_chunks(text: str) -> list[str]:
    """Split text into word-limited chunks with sentence-based overlap."""

    # Step 1: Split text into sentences.
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    # Step 2: Split any oversized sentence into smaller pieces.
    processed_sentences = []

    for sentence in sentences:
        words = sentence.split()

        if len(words) > CHUNK_SIZE:
            for i in range(0, len(words), CHUNK_SIZE):
                piece = " ".join(words[i : i + CHUNK_SIZE])
                processed_sentences.append(piece)
        else:
            processed_sentences.append(sentence)

    # Step 3: Build chunks.
    chunks = []
    current_sentences = []
    current_word_count = 0

    for sentence in processed_sentences:
        sentence = sentence.strip()

        if not sentence:
            continue

        sentence_word_count = len(sentence.split())

        # If adding this sentence exceeds the chunk limit,
        # save the current chunk and prepare overlap.
        if current_word_count + sentence_word_count > CHUNK_SIZE and current_sentences:
            chunks.append(" ".join(current_sentences))

            # Remove older sentences while preserving recent context.
            while current_sentences and current_word_count > CHUNK_OVERLAP:
                removed_sentence = current_sentences.pop(0)
                current_word_count -= len(removed_sentence.split())

        # Add the incoming sentence.
        current_sentences.append(sentence)
        current_word_count += sentence_word_count

    # Step 4: Save the final chunk.
    if current_sentences:
        chunks.append(" ".join(current_sentences))

    return chunks


text = """
Python is easy to learn. Python is useful for building AI applications.
Artificial intelligence allows computers to perform tasks that usually require human intelligence and reasoning in many different real-world situations across various industries today.
"""
print(create_chunks(text))
