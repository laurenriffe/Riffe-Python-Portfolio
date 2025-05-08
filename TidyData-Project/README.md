# 🏅 Tidy Data Olympics Project

Welcome to the **Tidy Data Olympics Project**, a Python-based data cleaning and visualization initiative centered around medalist data from the 2008 Summer Olympics. This project showcases how tidy data principles transform messy, multi-dimensional data into an organized, analysis-ready format — empowering deeper insights through better structure.

---

## 🧠 Purpose & Learning Outcomes

This project demonstrates:
- Core data tidying techniques using the `pandas` library
- Applying Hadley Wickham's tidy data principles in practice
- Effective reshaping, filtering, and organizing of tabular datasets
- Constructing meaningful visualizations that highlight patterns in gender, sport, and medal distribution

Designed as a teaching tool and data storytelling exercise, this project exemplifies clarity, cleanliness, and visual polish.

---

## 📊 Project Overview

The dataset originally presents medalist data in a wide format. This project walks through the full process of converting it into a tidy format where:
- Each variable has its own column
- Each observation has its own row
- Each type of observational unit forms a single table

After cleaning, visualizations are generated to explore trends across sports and genders, providing insight into Olympic representation.

---

## 🎯 Features

- 🔄 **Data Reshaping** using `melt()` and DataFrame transformations
- 🧼 **Missing Value Handling** and column cleanup
- 👥 **Gender/Sport Variable Extraction** from unstructured columns
- 📊 **Matplotlib & Seaborn Visualizations** with polished aesthetics
- 🧠 **Educational Code** with inline comments and clear logic

---

## 🧰 Tech Stack

| Tool        | Purpose                                   |
|-------------|-------------------------------------------|
| `Python`    | Core scripting and data processing        |
| `pandas`    | Data manipulation and reshaping           |
| `matplotlib`| Plotting visualizations                   |
| `seaborn`   | Advanced graphing and styling             |

---

## 📁 Project Directory Structure

```
TidyData-Project/
├── TidyData-Project.py       # Main Python script
├── olympics_2008.csv         # Raw dataset (before cleaning)
└── README.md                 # This documentation file
```

---

## ⚙️ How to Run This Project

### 1. Clone the Repository
```
git clone https://github.com/laurenriffe/Riffe-Python-Portfolio.git
cd Riffe-Python-Portfolio/TidyData-Project
```

### 2. Install Required Libraries
```
pip install pandas matplotlib seaborn
```

### 3. Run the Python Script
```
python TidyData-Project.py
```

The script will load the raw data, perform cleaning and transformation, and output summary visuals.

---

## 🧾 Dataset Details

- **Source**: 2008 Summer Olympics Medalists (CSV file)
- **Pre-Processing Includes**:
  - Converting wide data into tidy long format using `melt()`
  - Dropping missing or redundant entries
  - Parsing column names to extract gender and sport information
  - Renaming columns for consistency and clarity
  - Saving the cleaned dataset as a `.csv` for further use

---

## 🎨 Visualization Highlights

- **Medal Distribution by Sport** – Top sports based on total medals
- **Gender Distribution** – Side-by-side comparisons of medal counts by gender

> Screenshots and visual outputs can be included here.

---

## 📌 Requirements
- Python 3.7+
- pandas
- matplotlib
- seaborn

Install using:
```
pip install pandas matplotlib seaborn
```

---

## ❤️ Why This Project Stands Out
- ✅ Cleanly demonstrates **tidy data concepts**
- ✅ Turns **raw Olympic data into readable insights**
- ✅ Ideal for students, analysts, or anyone learning data wrangling
- ✅ Fully reproducible and documented

---

## 🔗 References
- [Tidy Data by Hadley Wickham (PDF)](https://vita.had.co.nz/papers/tidy-data.pdf)
- [Pandas Cheat Sheet (PDF)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

---

## 👩‍💻 About the Creator

Lauren Riffe is a Finance major at the University of Notre Dame with minors in Computing & Digital Technologies and Theology. Passionate about data storytelling, Lauren builds thoughtful, well-documented tools that highlight both technical proficiency and aesthetic care.

📫 [lriffe@nd.edu](mailto:lriffe@nd.edu)  
🔗 [LinkedIn](https://www.linkedin.com/in/lauren-riffe)

---
