<h1>Slight-Dynamic: Aerospace & Defense Stock Analysis 📊</h1>

![Stock Analysis](image/stock.gif)

## Project Goal
Identify **resilient, high-growth stocks** within the **Aerospace & Defense industry** using **data-driven financial analysis**.
We focus on stocks with **positive momentum**, **strong Free Cash Flow**, **healthy Gross Margins**, and **rising trading volumes**.

## 📘 Git Push & Pull Instructions

## 🧭 Prerequisites
- Git is installed on your machine and run the installer.
  
On Windows:
```bash
open https://git-scm.com
```
On macOS:
Use Homebrew:
```bash
brew install git
```
- Then run this to get all the latest project files:
```bash
git clone https://github.com/blkpvnthr/Slight-Dynamic.git
```
- Then make sure you're inside the project directory in your terminal.
```bash
cd Slight-Dynamic
```
- Then type this to see all the project files at once in the terminal.
```bash
ls
```

---

## 🔄 1. Pulling Changes (Get Latest from Remote)

Use this when you want to update your local copy with the latest changes from the remote repository:

This will show you all your local changes.
```bash
git status
```
if you have changes you havent pushed yet you need to stash them first 
```bash
git stash
```
Then pull the latest changes.
```bash
git pull 
```
Once the pull is complete, you can reapply your stashed changes:
```bash
git stash pop
```
⚠️ If there are conflicts after stash pop, Git will ask you to resolve them manually.

## 🛠️ To resolve merge conflicts:
Open each conflicted file — Git will mark the conflicting sections like this:
```bash
<<<<<<< HEAD
Your local changes
=======
Incoming changes from the branch
>>>>>>> branch-name
```
Manually edit the file to keep the correct code and remove the conflict markers (<<<<<<<, =======, >>>>>>>)...

After fixing all conflicts, stage the resolved files. You can enter them one by one like this:
```bash
git add <filename>
```
Or you can add them all at once like this:
```bash
git add .
```
Or if you created a specific folder you only want to push.. (be sure to add the after the folder name '/*' )
```bash
git add <foldername/*>
```
## ✅     Pushing Your Contributions

Be sure to check the status before you commit and before you push
```bash
git status
```
Then commit the merge:
```bash
git commit -m "Resolved merge conflicts after stash pop"
```
Then you can push your changes
```bash
git push
```
Then check the status again to be sure all conflicts are resolved
```bash
git status
```
## Project Overview
This repository contains our **CMSC206 Group Project**, which analyzes **aerospace and defense stock data** to uncover **high-performing assets**.

We use **Python** along with libraries like **Pandas**, **Matplotlib**, **YFinance**, and **PyPortfolioOpt** to:<br>
✅ Extract and clean data<br>
✅ Perform financial filtering<br>
✅ Visualize stock trends<br>
✅ Optimize portfolio allocations --> this is dependent upon what you guys decide you wanna do?<br>

## Quick Start &nbsp; 🏁

### 1️⃣  &nbsp; Clone the Repository
```bash
git clone https://github.com/blkpvnthr/Slight-Dynamic.git
cd Slight-Dynamic
```
<hr>

### 2️⃣  &nbsp; Python Version Requirement
⚠️ This project requires Python 3.8+. Verify your Python version:
```bash
python --version
```
If you don't have Python 3.8 or higher, install the latest version from the <a href="https://www.python.org/downloads/">Python download</a> page.

<em><b>📝 Windows Users❗</b>:
During installation, make sure to check the box that says “Add Python to PATH”.
Use python and pip commands in Command Prompt (cmd.exe) or PowerShell.</em>
<hr>

### 3️⃣ &nbsp;  Environment Setup
You can automatically set up the environment or do it manually.

#### &nbsp;  ✅ Option A: Automatic Setup
&nbsp; Run the env_setup.py script (works on both Windows & Mac/Linux):
```bash
python env_setup.py
```
&nbsp; This script will:<br>
        - Check Python version<br>
        - Create a virtual environment called project-env<br>
        - Install all necessary dependencies

# OR

#### &nbsp; ✅ Option B: Manual Setup
```bash
python -m venv project-env
pip install -r requirements.txt
```
&nbsp; This will install all the necessary packages provided you have Python installed.

<hr>

### 4️⃣ &nbsp; Activate the Virtual Environment
Always activate the project-env virtual environment before running any commands or notebooks.<br>
For Mac/Linux users:
```bash
source project-env/bin/activate
```
For Windows users:
```bash
project-env\Scripts\activate
```
<hr>

### 5️⃣ &nbsp; Run Jupyter Notebook
Once your virtual environment is active, start Jupyter by running:
```bash
jupyter notebook
```
In the Jupyter interface that opens in your browser, select the notebook file:
```bash
aerospace.ipynb
```

## 🔹 Features:

- 📊 **Stock Data Extraction** from Google Sheets & CSV
- 🔎 **Financial Health Filtering** (FCF, Gross Margins)
- 📡 **Industry-Specific Insights** (Defense & Aerospace)
- 📈 **Price Trend Analysis** (SMA, Volume Changes) ---> This is yet to be implemented.
- 💸 **Portfolio Optimization** (Sharpe Ratio & Risk Models) ---> This is yet to be implemented.

## Technologies Used

|   Technology       |  Description                   |
|--------------------|----------------------------------|
| Python 🐍 (>=3.8)  | Core programming language        |
| Pandas 🐼          | Data manipulation and analysis   |
| Matplotlib 📊      | Data visualization               |
| YFinance 💰        | Stock data extraction            |
| PyPortfolioOpt 📈  | Portfolio optimization           |
| Jupyter 📚         | Interactive notebook interface   |

## Authors

Eduardo Paz<br>
Asmaa Abdul-Amin<br>
Parker Link<br>
Ahmed Sachit<br>
Alhassane Moulaye<br>

## 🚨 Additional Notes
Make sure you're using Python 3.8+ for compatibility.

## License
📜 MIT License
