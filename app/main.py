from fastapi import FastAPI
from app.schema import Note
from app.storage import save_notes

app = FastAPI()

@app.get("/")
def root():
    return {"message":"ok"}

@app.post("/notes")
def create_note(note:Note):
    file_path = save_notes(
        filename = note.filename,
        content = note.content
    )
    return {"message":"note saved","filename":file_path.name}