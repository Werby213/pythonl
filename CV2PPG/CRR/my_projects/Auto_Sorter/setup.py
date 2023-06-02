from cx_Freeze import setup, Executable

setup(
    name="My Application",
    version="0.1",
    description="My Application Description",
    executables=[Executable("my_script.py")],
    options={
        "build_exe": {
            "includes": ["my_module"]
        }
    }
)
