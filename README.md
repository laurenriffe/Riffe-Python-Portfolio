# Riffe-Python-Portfolio

This repository will encompass all my completed coding projects. Organized by folders and a short description for each project, I will showcase data analysis skills and Python proficiency.
---
## How This Portfolio is Structured  
This portfolio showcases my data analysis and Python proficiency through multiple projects. The **Pet Finder Project** demonstrates my ability to build interactive web applications using Streamlit, while the **Tidy Data Project** highlights my skills in data cleaning, structuring, and visualization. Each project contributes to a well-rounded coding portfolio that reflects my growing expertise in Python programming and data analysis.


# Pet Finder Project  

## Project Overview  
The **Pet Finder Project** is a Streamlit-based web app designed to help users find their perfect pet by filtering available pets based on size. The application utilizes a dataset containing various pet attributes, making it easier to explore and compare different options.  

[View the Pet Finder Project Repository](<https://github.com/laurenriffe/Riffe-Python-Portfolio/tree/main/basic_streamlit_app>)  


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

# Tidy Data Project  

## Project Overview  
The **Tidy Data Project** focuses on cleaning and visualizing data from the 2008 Olympics medalists dataset. The goal is to ensure the dataset adheres to tidy data principles by structuring it properly—each variable has its own column, each observation is in a separate row, and each data type is consistent. The project also includes visualizations to highlight key insights from the cleaned data.  

[View the Tidy Data Project Repository](<https://github.com/laurenriffe/Riffe-Python-Portfolio/tree/main/TidyData-Project>)  

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
<img width="1108" alt="Distribution by Sport" src="https://github.com/user-attachments/assets/9fc86f55-120b-475d-be73-131cd0a59076" />


### Medal Distribution by Gender  
<img width="725" alt="Medal Distribution by Gender" src="https://github.com/user-attachments/assets/52c67414-3fcc-472f-b271-02e836458c05" />


---



