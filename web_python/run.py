import subprocess

def list_dir():
    result = subprocess.run(["ls", "-l"], capture_output=True)
    return result.stdout.decode('utf-8')