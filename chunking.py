import re

CHUNK_SIZE = 15
CHUNK_OVERLAP = 5


def create_chunks(text: str) -> list[str]:
    """Create sentence-aware chunks with a word limit and overlap."""

    # Step 1: Handle empty input.
    if not text.strip():
        return []

    # Step 2: Split text into sentences.
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    # Step 3: Split oversized sentences with word-based overlap.
    units = []

    for sentence in sentences:
        sentence_words = sentence.split()

        if len(sentence_words) > CHUNK_SIZE:
            step = CHUNK_SIZE - CHUNK_OVERLAP

            for i in range(0, len(sentence_words), step):
                piece_words = sentence_words[i : i + CHUNK_SIZE]
                units.append(" ".join(piece_words))

                # Stop when we've included the final word.
                if i + CHUNK_SIZE >= len(sentence_words):
                    break
        else:
            units.append(sentence)

    # Step 4: Combine sentence units into chunks.
    chunks = []
    current_units = []
    current_word_count = 0

    for unit in units:
        unit_word_count = len(unit.split())

        if current_word_count + unit_word_count <= CHUNK_SIZE:
            current_units.append(unit)
            current_word_count += unit_word_count
            continue

        # Save the current chunk.
        if current_units:
            chunks.append(" ".join(current_units))

        # Step 5: Carry over complete units within the overlap budget.
        overlap_units = []
        overlap_word_count = 0

        for previous_unit in reversed(current_units):
            previous_count = len(previous_unit.split())

            if overlap_word_count + previous_count > CHUNK_OVERLAP:
                break

            overlap_units.insert(0, previous_unit)
            overlap_word_count += previous_count

        # Ensure overlap plus the new unit does not exceed the limit.
        while overlap_units and overlap_word_count + unit_word_count > CHUNK_SIZE:
            removed_unit = overlap_units.pop(0)
            overlap_word_count -= len(removed_unit.split())

        current_units = overlap_units + [unit]
        current_word_count = overlap_word_count + unit_word_count

    # Step 6: Save the final chunk.
    if current_units:
        chunks.append(" ".join(current_units))

    return chunks


# Test
text = """
Python is easy to learn. Python is useful for building AI applications.
Artificial intelligence allows computers to perform tasks that usually require
human intelligence and reasoning in many different real-world situations
across various industries today.
"""

chunks = create_chunks(text)

for index, chunk in enumerate(chunks, start=1):
    word_count = len(chunk.split())
    print(f"Chunk {index} ({word_count} words):")
    print(chunk)
    print()

    assert word_count <= CHUNK_SIZE
