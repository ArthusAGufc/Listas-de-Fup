import os
import pkg_resources  # Replaces pip.get_installed_distributions()
from pathlib import Path

def get_package_size(path):
    """Calcula o tamanho de um diretório (em MB)."""
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size / (1024 * 1024)  # Converte bytes para MB

# Get installed packages and their locations
packages = {pkg.project_name: pkg.location for pkg in pkg_resources.working_set}
packages_info = []

for package, location in packages.items():
    package_path = Path(location) / package
    if package_path.exists():
        size = get_package_size(package_path)
        packages_info.append((package, size, package_path))

# Sort by package size in descending order
packages_info.sort(key=lambda x: x[1], reverse=True)

# Print results
print(f"{'Pacote':<30}{'Tamanho (MB)':<15}{'Local'}")
print("=" * 80)
for pkg, size, path in packages_info:
    print(f"{pkg:<30}{size:<15.2f}{path}")
