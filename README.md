# UEFA Champions League SQL GUI

This project is a Python application with a Tkinter-based GUI connected to a Microsoft SQL Server database for UEFA Champions League data.

An interactive desktop application built with **Python**, **SQL Server**, and **Tkinter** that connects a relational database of UEFA Champions League data with a user-friendly GUI. The project showcases advanced SQL querying, OLAP analytics, and data entry workflows.

## 🎯 Project Overview

This app was created for the course **Relational Database Implementation and Applications**. It demonstrates how to design a normalized database schema, populate it with structured data, and interact with it via a Python GUI.

## 🧩 Key Features

- 🔐 Password-protected login interface
- 📊 Execute complex SQL queries via buttons:
  - Set operations (UNION, INTERSECT)
  - Subqueries with `WITH` clause
  - Aggregate functions and OLAP (ROLLUP)
- 👥 Add new players through a custom input form
- ⚽ Insert random or manual goal records into the database
- 🖥️ Results displayed in styled tables (Treeview)
- 🎨 Clean GUI design with logo, fonts, and formatting

## 🛠️ Tools & Technologies

| Tool              | Purpose                          |
|-------------------|----------------------------------|
| Python            | Backend logic & GUI (Tkinter)    |
| SQL Server        | Relational database              |
| pyodbc            | Database connection driver       |
| SQL               | Data manipulation & queries      |
| Tkinter           | GUI development                  |

## 🖼️ Screenshots

## ERD:

![image](https://github.com/user-attachments/assets/05ad0973-122c-48b2-822d-6c6b930bf404)

## Login Access:

![image](https://github.com/user-attachments/assets/b04b3807-6f0e-4760-b818-10f82044f8ba)

## Application:

![image](https://github.com/user-attachments/assets/2a76c797-4ae0-42fc-856e-4f24ca190eb8)

## Query Request:

![image](https://github.com/user-attachments/assets/66576906-1f8c-4e50-9827-c5aea01a20bc)

## Insert Records:

![image](https://github.com/user-attachments/assets/e0a5ad25-901e-4aa0-9f16-64777b7405eb)


## 🧠 What I Learned

- Designing normalized relational schemas
- Writing and optimizing complex SQL queries
- Connecting Python to SQL Server with `pyodbc`
- Building user-friendly interfaces for data apps
- Using OLAP tools like `ROLLUP` for multi-level aggregation

## 📦 Folder Structure

```
uefa_app/
├── app.py               # Main GUI app
├── db_config.py         # Database connection
├── queries.py           # All SQL queries
├── README.md            # Project documentation
└── screenshots/         # Images for demo
```
![image](https://github.com/user-attachments/assets/ec331a5c-5283-456e-bb65-7b6e67acd7b1)


## 📁 Future Enhancements

- Export query results to CSV/Excel
- Add charts with matplotlib
- Build web version with Flask or Streamlit
- Add full authentication system

## 👋 About Me

I'm a data science enthusiast with a strong interest in databases, analytics, and building real-world tools. This project showcases the foundational skills that power any robust data pipeline.


## Requirements
- Python 3.x
- `pyodbc` package
- Microsoft SQL Server with appropriate schema and data

## Setup
1. Update your server name in `db_config.py`.
2. Ensure the database `UEFA_Champion_League` is available.
3. Run `app.py` to launch the GUI.

## Functionality
- View referees who have not officiated any match.
- Add more queries to `queries.py` and GUI buttons in `app.py`.
