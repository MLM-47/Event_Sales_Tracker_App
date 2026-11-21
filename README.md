# 📈 LJ Events Sales Tracker

A lightweight, browser-based web application built with **Python** and **Streamlit** to help event businesses log bookings, track expenses, and analyze net profit by event category in real time.

---

## ✨ Features

* **View All Sales:** Interactive, full-width data table displaying all recorded event sales alongside total transaction counts.
* **Add New Sales:** Validated input form capturing client name, event category, event date, selling price, and expenses with automatic form clearing.
* **Update Records:** Dropdown selector (`#ID - Client Name`) that pre-fills existing record details for quick edits and validation.
* **Safe Deletion:** Confirmation checkbox safeguard before permanently removing mistaken entries.
* **Profit Analytics:** Automatically aggregates sales count, total revenue, expenses, and net profit grouped by event category, sorted from highest to lowest profit.

---

## 🛠️ Tech Stack

* **Frontend & App Framework:** [Streamlit](https://streamlit.io)
* **Language:** Python 3.9+
* **Database:** SQLite (`sqlite3`) via custom `database.py` module

---

## 📂 Project Structure

```text
Event_Sales_Tracker_App/
├── main.py          # Main Streamlit application & UI tabs
├── database.py      # SQLite database connection and CRUD operations
├── sales.db         # Auto-generated SQLite database file
└── README.md        # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have Python installed on your machine, then install Streamlit:

```bash
pip install streamlit
```

### 2. Clone or Download the Project
Navigate to your project folder in the terminal:

```bash
cd Event_Sales_Tracker_App
```

### 3. Run the Application
Start the Streamlit local server:

```bash
streamlit run main.py
```

The app will automatically open in your default web browser at `http://localhost:8501`.

---

## 💡 Usage Guide

1. **Add Tab:** Enter the client's name, event category (e.g., *Wedding*, *Corporate*, *Birthday*), date, selling price, and expenses, then click **Add sale**.
2. **View Tab:** Review all logged transactions and check your overall sale count.
3. **Update Tab:** Select an existing sale from the dropdown (`#ID - Client Name`), modify any field, and click **Save changes**.
4. **Delete Tab:** Select a record, tick the confirmation checkbox, and click **Delete**.
5. **Profit Tab:** View automated profit breakdowns ranked by event category.

---

## 🗺️ Roadmap

* [ ] Add top-level KPI metric cards (Total Revenue, Total Expenses, Net Profit, Profit Margin %)
* [ ] Add interactive bar charts comparing profit across event categories
* [ ] Export sales and profit reports to CSV/Excel
* [ ] Add date-range and category filters to the View tab

---

## 📄 License

This project is open-source and available for educational and personal business use.
