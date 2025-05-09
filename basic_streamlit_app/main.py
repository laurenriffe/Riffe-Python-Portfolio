import streamlit as st
import pandas as pd

# ================================
# Step 1: Displaying a Simple DataFrame in Streamlit
# ================================
st.title("Pet Finder 🐶 🐱 ")
st.subheader("The following data shows different types of pets and allows you to sort by size in order to find your perfect pet!")

# Creating a simple DataFrame manually
# This helps students understand how to display tabular data in Streamlit.
df = pd.DataFrame({
    'Pet name': ['CUPCAKE', '*ROCKEFELLER', 'TRIXIE', 'TOBIAS'],
    'Pet Size': ['LARGE', 'MED', 'SMALL', 'MED'],
    'Color': ['BLACK', 'TAN', 'ORANGE', 'WHITE / BRINDLE']
})

# Displaying the table in Streamlit
# st.dataframe() makes it interactive (sortable, scrollable)
st.write("Here's a simple table:")
st.dataframe(df)

# ================================
# Step 2: Adding User Interaction with Widgets
# ================================

# Using a selectbox to allow users to filter data by city
# Students learn how to use widgets in Streamlit for interactivity
size = st.selectbox("Select a size", df["Pet Size"].unique())

# Filtering the DataFrame based on user selection
filtered_df = df[df["Pet Size"] == size]

# Display the filtered results
st.write(f"Pets that are {size}:")
st.dataframe(filtered_df)

# ================================
# Step 3: Importing Data Using a Relative Path
# ================================

# Now, instead of creating a DataFrame manually, we load a CSV file
# This teaches students how to work with external data in Streamlit
df = pd.read_csv("data/pets.csv")  # Ensure the "data" folder exists with the CSV file
# Display the imported dataset
st.write("Here's the dataset loaded from a CSV file:")
st.dataframe(df)



# Using a selectbox to allow users to filter data by city
# Students learn how to use widgets in Streamlit for interactivity
size = st.selectbox("Select a size", df["Pet Size"].unique(), key="size_selectbox_csv")
# Filtering the DataFrame based on user selection
filtered_df = df[df["Pet Size"] == size]

# Display the filtered results
st.write(f"People in {size}:")
st.dataframe(filtered_df)

# ================================
# Summary of Learning Progression:
# 1️⃣ Displaying a basic DataFrame in Streamlit.
# 2️⃣ Adding user interaction with selectbox widgets.
# 3️⃣ Importing real-world datasets using a relative path.
# ================================