from cx_Freeze import setup, Executable

setup(
    name = "question",
    version = "0.1",
    description = "Question",
    executables = [Executable("question.py")]
)