import subprocess

def test_hello_world():
    bash_command = "./src/hello"
    output = subprocess.getoutput(bash_command)
    assert output == "world"
