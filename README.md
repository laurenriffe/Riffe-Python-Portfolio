# Riffe-Python-Portfolio
This repository will encompass all my completed coding projects. Organized by folders and a short description for each project, I will showcase data analysis skills and Python proficiency. 

Here's a README description for your Pet Finder Project:  

---

# Pet Finder Project  

## Project Overview  
The **Pet Finder Project** is a Streamlit-based web app designed to help users find their perfect pet by filtering available pets based on size. The application utilizes a dataset containing various pet attributes, making it easier to explore and compare different options.  

## Instructions  
To run the project, follow these steps:  
1. Ensure you have Python installed on your system.  
2. Install the required dependencies using:  
   ```bash
   pip install streamlit pandas
   ```  
3. Navigate to the project directory and run the Streamlit app with:  
   ```bash
   streamlit run main.py
   ```  

## Dataset Description  
The dataset includes information on various pets, including their size, breed, and other characteristics. Users can filter pets based on their preferences to find the best match.  

## References  
For more details on Streamlit, check out:  
- [Streamlit Documentation](https://docs.streamlit.io/)  

---

Let me know if you need any modifications!


# Tidy Data Project Repository

## Project Overview
This project focuses on cleaning and visualizing data from the 2008 Olympics medalists dataset. The goal is to ensure the dataset adheres to tidy data principles by structuring it properly—each variable has its own column, each observation is in a separate row, and each data type is consistent. The project also includes visualizations to highlight key insights from the cleaned data.

## Instructions
### Prerequisites
Ensure you have the following dependencies installed:
- Python 3.x
- pandas
- matplotlib
- seaborn

You can install the required packages using:
```bash
pip install pandas matplotlib seaborn
```

### Running the Notebook
1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd TidyData-Project
   ```
3. Run the Python script:
   ```bash
   python TidyData-Project.py
   ```

## Dataset Description
- **Source:** The dataset contains information on medalists from the 2008 Olympics.
- **Pre-processing Steps:**
  - Data reshaping using the `melt()` function.
  - Handling missing values by dropping them.
  - Extracting relevant attributes (e.g., gender and sport) from column names.
  - Cleaning column values for readability.
  - Saving the cleaned dataset for further use.

## References
- [Tidy Data Principles by Hadley Wickham](https://vita.had.co.nz/papers/tidy-data.pdf)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

## Visual Examples
### Medal Distribution by Sport
![Medal Distribution by Sport](visuals/medals_by_sport.png)

### Medal Distribution by Gender
![Medal Distribution by Gender](visuals/medals_by_gender.png)

This project demonstrates the application of tidy data principles and effective visualization techniques to extract meaningful insights from Olympic medal data.

