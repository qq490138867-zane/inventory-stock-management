# Inventory Stock Management System

## Project Overview

This project is a Python-based Inventory Stock Management System developed for the IY499 Introduction to Programming module.

The system allows users to manage products through a simple command-line interface. Data is stored in a JSON file so that the inventory is saved between program executions.

The project demonstrates object-oriented programming, modular programming, file handling, searching, sorting, data validation and data visualisation.


---

## Features

- Add new products
- View all products
- Search products by ID or name
- Update existing products
- Delete products
- Low stock report
- Sort products by:
  - Name
  - Price
  - Quantity
- Inventory stock bar chart
- Automatic JSON data saving
- Input validation and error handling


---

## Project Structure

```
inventory-stock-management/
│
├── data/
│   └── inventory.json
│
├── file_handler.py
├── inventory_manager.py
├── search_sort.py
├── charts.py
├── gui.py
├── utils.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python 3
- JSON
- Matplotlib

---

## Installation

Install the required package:

```bash
pip install -r requirements.txt
```

---

## Running the Program

Run the program using:

```bash
python main.py
```

---

## Program Functions

The system supports the following operations:

1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Low Stock Report
7. Sort Products
8. Stock Chart
9. Exit

---

## Data Storage

All inventory data is stored in:

```
data/inventory.json
```

Changes are automatically saved whenever products are added, updated or deleted.

---

## Future Improvements

Possible future improvements include:

- Graphical User Interface (GUI)
- Database support
- User authentication
- Export inventory reports
- More advanced search filters

---

## Author

Qian Cao

University of York

Module: IY499 Introduction to Programming
