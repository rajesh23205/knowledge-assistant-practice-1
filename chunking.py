def create_chunks(text: str) -> list[str]:
    """Split the text into word limited chunks with sentance-based overlap."""

    print(text)


text = """
Accept a string of text.
Split it into chunks using a configurable chunk size.
Support overlap so some content is carried into the next chunk.
Return a list of strings.
"""
create_chunks(text)
