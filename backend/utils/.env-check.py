# utils/env-check.py

import sys
import os
import subprocess
import importlib.util
import re
from pathlib import Path

# --- Config ---
REQUIREMENTS_FILE = Path(__file__).resolve().parents[2] / "requirements.txt"

# Package-to-import-name map
PACKAGE_IMPORT_MAP = {
    "attrs": "attr",
    "black": "black",
    "cattrs": "cattrs",
    "certifi": "certifi",
    "charset-normalizer": "charset_normalizer",
    "click": "click",
    "geographiclib": "geographiclib",
    "geopy": "geopy",
    "idna": "idna",
    "immanuel": "immanuel",
    "iniconfig": "iniconfig",
    "kerykeion": "kerykeion",
    "mypy-extensions": "mypy_extensions",
    "numpy": "numpy",
    "packaging": "packaging",
    "pathspec": "pathspec",
    "platformdirs": "platformdirs",
    "pluggy": "pluggy",
    "pydantic": "pydantic",
    "pydantic-core": "pydantic_core",
    "pytest": "pytest",
    "python-dotenv": "dotenv",
    "pytz": "pytz",
    "requests": "requests",
    "scour": "scour",
    "setuptools": "setuptools",
    "six": "six",
    "timezonefinder": "timezonefinder",
    "typing-extensions": "typing_extensions",
    "urllib3": "urllib3",
    "wheel": "wheel"
}

def check_module(module_name: str) -> bool:
    """Check if a module is importable."""
    try:
        return importlib.util.find_spec(module_name) is not None
    except Exception:
        return False

def parse_requirements_file(path: Path) -> list[str]:
    """Extract package names from requirements.txt."""
    modules = []
    if not path.exists():
        return modules
    with open(path, 'r') as file:
        for line in file:
            line = line.strip().split('#')[0].strip()
            if not line:
                continue
            if line.startswith("git+") or "@" in line:
                # Handle VCS-style or editable installs
                match = re.search(r'#egg=([a-zA-Z0-9_\-]+)', line)
                if match:
                    modules.append(match.group(1).lower())
                else:
                    name_match = re.search(r'/([a-zA-Z0-9_\-]+)(\.git)?', line)
                    if name_match:
                        modules.append(name_match.group(1).lower())
            else:
                mod = re.split(r'[<>=]', line)[0].strip()
                if mod:
                    modules.append(mod.lower())
    return modules

def main():
    print("🔍 Python Environment Check\n")

    # Basic info
    print(f"🔗 Python Path     : {sys.executable}")
    print(f"📦 Python Version  : {sys.version.split()[0]}")
    if tuple(map(int, sys.version.split(".")[:2])) >= (3, 13):
        print("⚠️  Python 3.13+ detected — some libraries like pyswisseph may break.\n")

    pip_path = subprocess.getoutput("which pip")
    print(f"📦 Pip Path        : {pip_path}")
    
    conda_env = os.environ.get("CONDA_DEFAULT_ENV")
    print(f"{'🟢' if conda_env else '🔴'} Conda Environment: {conda_env or 'Not active'}\n")

    # Parse and check
    print("📦 Package Checks:")
    packages = parse_requirements_file(REQUIREMENTS_FILE)
    if not packages:
        print(f"⚠️  No packages found in {REQUIREMENTS_FILE}")
        return

    missing = []
    for pkg in sorted(set(packages)):
        import_name = PACKAGE_IMPORT_MAP.get(pkg, pkg)
        is_installed = check_module(import_name)
        print(f"   - {pkg:<15}: {'✅ FOUND' if is_installed else '❌ MISSING'}")
        if not is_installed:
            missing.append(pkg)

    if missing:
        print("\n💡 TIP: To install missing modules, run:")
        print(f"   python -m pip install {' '.join(missing)}")
    else:
        print("\n✅ All required packages are installed.")

if __name__ == "__main__":
    main()
