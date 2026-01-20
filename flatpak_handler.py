import subprocess

def search_flatpak(package):
    result = subprocess.run(
        ["flatpak", "search", package],
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