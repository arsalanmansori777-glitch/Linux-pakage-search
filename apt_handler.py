import subprocess

def search_apt(package):
    result = subprocess.run(
        ["apt", "search", package],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

    packages = []
    for line in result.stdout.splitlines():
        if "/" in line and not line.startswith("Sorting"):
            name = line.split("/")[0]
            packages.append(name)

    return packages