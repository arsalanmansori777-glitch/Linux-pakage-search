from apt_handler import search_apt
from flatpak_handler import search_flatpak
from snap_handler import search_snap

package = input("Enter package name: ")

print("\nAPT results:")
for p in search_apt(package):
    print("-", p)

print("\nFlatpak results:")
for p in search_flatpak(package):
    print("-", p)

print("\nSnap results:")
for p in search_snap(package):
    print("-", p)

snap_results = search_snap(package)
if snap_results:
    for p in snap_results:
        print("-", p)
else:
    print("No Snap packages found.")