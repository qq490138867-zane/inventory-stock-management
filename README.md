# Inventory Stock Management System

## Project Overview

This project is a Python-based Inventory Stock Management System developed for the IY499 Introduction to Programming module at the University of York.

The system allows users to manage inventory through a simple command-line interface. It demonstrates object-oriented programming, modular programming, file handling, searching and sorting algorithms, data validation, error handling, and data visualisation. All inventory data is stored in a JSON file, allowing information to be automatically saved and loaded between program executions.

## GitHub Repository

The source code for this project is available at:

https://github.com/qq490138867-zane/inventory-stock-management

## Features

- Add new products
- View all products
- Search products by ID or name
- Update existing products
- Delete products
- Generate a low stock report
- Sort products by:
  - Name
  - Price
  - Quantity
- Display an inventory stock bar chart
- Automatic JSON data saving
- Input validation and error handling

## Project Structure

```
inventory-stock-management/
│
├── data/
│   └── inventory.json
├── file_handler.py
├── inventory_manager.py
├── search_sort.py
├── charts.py
├── main.py
├── requirements.txt
└── README.md
```

## Technologies Used

- Python 3
- JSON
- Matplotlib

## Installation

Install the required package:

```
pip install -r requirements.txt
```

## Running the Program

Run the program using:

```
python main.py
```

## Program Functions

The system supports the following operations:

- Add Product
- View Products
- Search Product
- Update Product
- Delete Product
- Low Stock Report
- Sort Products
- Stock Chart
- Exit

## Data Storage

All inventory data is stored in:

```
data/inventory.json
```

Changes are automatically saved whenever products are added, updated or deleted.

## Future Improvements

Possible future improvements include:

- Graphical User Interface (GUI)
- Database support
- User authentication
- Export inventory reports
- Advanced search and filtering options

## Author

**Name:** Qian Cao

**P-Number:** P303070378

**Module:** IY499 Introduction to Programming

## Academic Integrity

I confirm that this assignment is my own work.

Where I have referred to online sources, I have provided comments detailing the reference and included a link to the source.
