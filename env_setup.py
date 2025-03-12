# Author: Asmaa Abdul-Amin
# Date: 2021-07-25
# Requirements: pip, numpy, pandas, matplotlib, scikit-learn, tensorflow, keras, yfinance, PyPortfolioOpt
# Usage: python install_libraries.py
# Notes: This script will install the required libraries if they are not already installed.
import sys
import subprocess
import platform
import os
import shutil

# Required Python version
REQUIRED_PYTHON_MAJOR = 3
REQUIRED_PYTHON_MINOR = 11

# List of required libraries
REQUIRED_LIBRARIES = [
    "pandas",
    "numpy",
    "matplotlib",
    "yfinance",
    "PyPortfolioOpt"
]

def check_python_version():
    """
    Checks if Python is installed and if it meets the minimum version requirement.
    """
    current_version = sys.version_info
    version_str = f"{current_version.major}.{current_version.minor}.{current_version.micro}"
    
    print(f"🔍 Detected Python version: {version_str}")

    if (current_version.major, current_version.minor) < (REQUIRED_PYTHON_MAJOR, REQUIRED_PYTHON_MINOR):
        print(f"❌ Python {REQUIRED_PYTHON_MAJOR}.{REQUIRED_PYTHON_MINOR} or higher is required.")
        suggest_python_install()
        sys.exit(1)
    else:
        print(f"✅ Python version is sufficient (>= {REQUIRED_PYTHON_MAJOR}.{REQUIRED_PYTHON_MINOR}).")


def suggest_python_install():
    """
    Provides installation instructions or automates installation for Python 3.11.
    """
    os_name = platform.system()

    print("\n⚠️ Python 3.11+ is required but not detected.")
    
    if os_name == "Linux":
        print("👉 Attempting to install Python 3.11 on Linux...")

        try:
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "software-properties-common"], check=True)
            subprocess.run(["sudo", "add-apt-repository", "-y", "ppa:deadsnakes/ppa"], check=True)
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "python3.11", "python3.11-venv", "python3.11-distutils"], check=True)
            
            print("\n✅ Python 3.11 installed. Run the script again using:")
            print("   python3.11 env_setup.py\n")
        except subprocess.CalledProcessError:
            print("❌ Failed to install Python 3.11 automatically.")
            print("👉 Please install it manually: https://www.python.org/downloads/release/python-3110/")
    
    elif os_name == "Darwin":  # macOS
        print("👉 Attempting to install Python 3.11 on macOS with Homebrew...")

        if shutil.which("brew") is None:
            print("❌ Homebrew is not installed. Please install Homebrew first: https://brew.sh/")
        else:
            try:
                subprocess.run(["brew", "update"], check=True)
                subprocess.run(["brew", "install", "python@3.11"], check=True)
                
                print("\n✅ Python 3.11 installed. Run the script again using:")
                print("   python3.11 env_setup.py\n")
            except subprocess.CalledProcessError:
                print("❌ Failed to install Python 3.11 automatically.")
                print("👉 Please install it manually: https://www.python.org/downloads/release/python-3110/")
    
    elif os_name == "Windows":
        print("👉 On Windows, please install Python 3.11 manually:")
        print("   Download Python 3.11 from https://www.python.org/downloads/windows/")
    
    else:
        print(f"❌ Unsupported OS: {os_name}")
        print("👉 Please install Python 3.11 manually from https://www.python.org/downloads/")


def install_and_import(libraries):
    """
    Installs and verifies required libraries.
    """
    for lib in libraries:
        try:
            __import__(lib)
            print(f"✔ {lib} is already installed.")
        except ImportError:
            print(f"✖ {lib} not found. Installing {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])


def main():
    print(f"🛠️  CMSC206 Environment Setup ({platform.system()} OS) 🛠️")
    
    # Step 1: Check Python version
    check_python_version()

    # Step 2: Install and verify required libraries
    install_and_import(REQUIRED_LIBRARIES)

    print("\n✅ Environment setup complete. You're ready to analyze data! 🚀📊\n")
    print("\nTo run the main script run: 'jupyter notebook' in the terminal, then select 'aerospace.ipynb' in the new Jupyter notebook interface.\n")


if __name__ == "__main__":
    main()
