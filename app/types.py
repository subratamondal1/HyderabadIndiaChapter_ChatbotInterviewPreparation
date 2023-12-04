from typing import Literal, TypedDict

from streamlit.runtime.uploaded_file_manager import UploadedFile


class UserData(TypedDict):
    fullname: str
    role: str
    experience: int | float
    about: str
    resume: UploadedFile | None
