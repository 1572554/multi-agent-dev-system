import subprocess

def run_pytest():
    result = subprocess.run(
        ["pytest"],
        capture_output=True,
        text=True
    )

    return result.stdout