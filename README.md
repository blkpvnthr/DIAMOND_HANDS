<h1>Slight-Dynamic: Aerospace & Defense Stock Analysis 📊</h1>

![Stock Analysis](image/stock.gif)

## 🚀 Project Goal
Identify **resilient, high-growth stocks** within the **Aerospace & Defense industry** using **data-driven financial analysis**.
We focus on stocks with **positive momentum**, **strong Free Cash Flow**, **healthy Gross Margins**, and **rising trading volumes**.

---

## 📂 Project Overview
This repository contains our **CMSC206 Group Project**, which analyzes **aerospace and defense stock data** to uncover **high-performing assets**.

We use **Python** along with libraries like **Pandas**, **Matplotlib**, **YFinance**, and **PyPortfolioOpt** to:
✅ Extract and clean data
✅ Perform financial filtering
✅ Visualize stock trends
✅ Optimize portfolio allocations

---

## Quick Start

### 1️⃣  &nbsp; Clone the Repository
```bash
git clone https://github.com/blkpvnthr/Slight-Dynamic.git
cd Slight-Dynamic
```

### 2️⃣  &nbsp; Python Version Requirement
⚠️ This project requires Python 3.8+. Verify your Python version:
```bash
python --version
```
If you don't have Python 3.8 or higher, install the latest version from the <a href="https://www.python.org/downloads/">Python download</a> page.

<em><b>📝 Windows Users❗</b>:
During installation, make sure to check the box that says “Add Python to PATH”.
Use python and pip commands in Command Prompt (cmd.exe) or PowerShell.</em>

### 3️⃣ &nbsp;  Environment Setup
You can automatically set up the environment or do it manually.

#### ✅ Option A: Automatic Setup
Run the env_setup.py script (works on both Windows & Mac/Linux):
```bash
python env_setup.py
```
This script will:
- Check Python version
- Create a virtual environment called project-env
- Install all necessary dependencies

#### ✅ Option B: Manual Setup
```bash
python -m venv project-env
pip install -r requirements.txt
```
This will install all the necessary packages provided you have Python installed.

### 4️⃣ &nbsp; Run Jupyter Notebook
Once your virtual environment is active, start Jupyter:
```bash
jupyter notebook
```
In the Jupyter interface that opens in your browser, select the notebook file:
```bash
aerospace.ipynb
```

## 🔹 Features:

- 📊 **Stock Data Extraction** from Google Sheets & CSV
- 📈 **Price Trend Analysis** (SMA, Volume Changes)
- 💰 **Financial Health Filtering** (FCF, Gross Margins)
- 📡 **Industry-Specific Insights** (Defense & Aerospace)
- 📉 **Portfolio Optimization** (Sharpe Ratio & Risk Models)

## 🛠 Technologies Used
✅ Technology	📝 Description
Python 🐍 (>=3.8)	Core programming language
Pandas 🏛	Data manipulation and analysis
Matplotlib 📊	Data visualization
YFinance 💹	Stock data extraction
PyPortfolioOpt 📈	Portfolio optimization
Jupyter 📒	Interactive notebook interface

## 👨‍💻 Authors
Eduardo Paz
Asmaa Abdul-Amin
Parker Link
Ahmed Sachit
Alhassane Moulaye

## ⚙️ Additional Notes
Make sure you're using Python 3.8+ for compatibility.
Always activate the project-env virtual environment before running any commands or notebooks.
For Windows users: Use cmd.exe or PowerShell and remember to activate with project-env\Scripts\activate.
For Mac/Linux users: Use source project-env/bin/activate.

## License
📜 MIT License