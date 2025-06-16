# 🎮 Xbox Series S Price Tracker (Walmart)

This bot tracks the **real-time price** of the Xbox Series S console on Walmart.com and logs the data to a CSV file. Built with Selenium and Python, this tool simulates browser behavior and grabs the current price from the product page.

> 🔗 **Target Product:**
[Xbox Series S 512 GB Console on Walmart](https://www.walmart.com/ip/443574645?sid=a049bd64-95cb-49c4-a1e5-6a50e961243a)

---

## ⚙️ What It Does

- Launches a headless Chrome browser
- Navigates to the Walmart product page
- Extracts the product name and current price
- Logs the result with a timestamp to `price_log.csv`
- Appends each run so you get a **price history** over time

---

## 🛠️ Technologies Used

- Python 3
- Selenium WebDriver
- ChromeDriver (via `webdriver-manager`)
- Pandas
- VS Code

---

## 💾 Output Example

The script generates a `price_log.csv` file like this:

| Date | Product | Price |
|---------------------|----------------------------------|--------|
| 2025-06-14 20:12:03 | Xbox Series S 512 GB Console | $289.00 |
| 2025-06-15 09:31:55 | Xbox Series S 512 GB Console | $288.50 |

---

## 🚀 How to Run It

### 1. Clone the Repo

```bash
git clone https://github.com/billiondollarjones/xbox-price-tracker.git
cd xbox-price-tracker

### 2. Install Dependencies

```bash
pip install selenium webdriver-manager pandas

### 3. Run the Script

```bash
python main.py

## A new entry will be added to price_log.csv every time you run it.
