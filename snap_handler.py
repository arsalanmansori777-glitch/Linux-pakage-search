import subprocess

def search_snap(package):
    result = subprocess.run(
        ["snap", "find", package],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

    packages = []
    for line in result.stdout.splitlines()[1:]:
        parts = line.split()
        if parts:
            packages.append(parts[0])

    return packages