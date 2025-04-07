<h1>Slight-Dynamic: Aerospace & Defense Stock Analysis 📊</h1>

![Stock Analysis](image/stock.gif)

## Project Goal
Identify **resilient, high-growth stocks** within the **Aerospace & Defense industry** using **data-driven financial analysis**.
We focus on stocks with **positive momentum**, **strong Free Cash Flow**, **healthy Gross Margins**, and **rising trading volumes**.

## 📘 Git Push & Pull Instructions

## 🧭 Prerequisites
- Git is installed on your machine.
- You’ve initialized a Git repository (`git init`) or cloned one (`git clone <repo-url>`).
- You're inside the project directory in your terminal.

---

## 🔄 1. Pulling Changes (Get Latest from Remote)

Use this when you want to update your local copy with the latest changes from the remote repository.

```bash
git pull origin <branch-name>
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
