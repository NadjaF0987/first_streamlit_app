
import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omege 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and rocket Smoothie')
streamlit.text('🐔 Hard-boilded Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# pick list
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# display the table on the page
streamlit.dataframe(my_fruit_list)
