def clean_text(text):
    return text.strip().lower()

def is_valid(entry):
    return isinstance(entry, str) and len(entry) > 0
