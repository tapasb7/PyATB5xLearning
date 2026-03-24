import subprocess

result = subprocess.run(
    ['ipconfig'],
    capture_output=True,
    text=True,
    timeout=30
    )
print(result.stdout)
print(result.stderr)
print(result.returncode)

if result.returncode != 0:
    print("Command failed")
else:
    print('Command succeeded')