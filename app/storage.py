from pathlib import Path

NOTES = Path("notes")

def save_notes(filename: str, content: str):
    NOTES.mkdir()
    file_path = NOTES / filename
    file_path.write_text(content,encoding="UTF-8")
    return file_path