# 🏁 F1 Database Management System

A Python-based application to manage and analyze Formula 1 (F1) racing data. The system provides both **Admin** and **User** modes for interacting with an F1 database containing detailed tables like cars, circuits, drivers, teams, winners, and fastest laps.

---

## 📋 Features

### Admin Mode:
- Add, update, and delete records from:
  - Cars
  - Circuits
  - Drivers
  - Fastest Laps
  - Teams
  - Winners

### User Mode:
- View records from all database tables
- Execute advanced SQL queries:
  - **Set Operations** (UNION, INTERSECT)
  - **Subqueries** for rankings and statistics
  - **OLAP & Window Functions** (rankings, rolling totals, partitioning)

---

## ⚙️ Installation

1. Make sure Python is installed.
2. Set up MySQL on your local machine or use an existing server.
3. Create a database named `C425_Project`.
4. Create the necessary tables as per schema.
5. Install Python dependencies:
   ```bash
   pip install mysql-connector-python tabulate
