def clean_text(text):
    """
    Removes extra spaces, tabs, and newlines.
    """

    cleaned = " ".join(text.split())

    return cleaned