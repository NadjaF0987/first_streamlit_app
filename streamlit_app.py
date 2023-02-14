
import streamlit
import pandas
import requests

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omege 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and rocket Smoothie')
streamlit.text('🐔 Hard-boilded Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table on the page
streamlit.dataframe(fruits_to_show)

fruityvice_reposnse = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_reponse)
