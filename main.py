import streamlit as st
from scraper import scrape_website, extract_body_content, clean_body_content


st.title("AI Web Scraper")

url = st.text_input("Enter the URL of the website you want to scrape:")

if st.button("Scrape"):
  st.write("Scraping...")
  result = scrape_website(url)
  body_content = extract_body_content(result)
  cleaned_content = clean_body_content(body_content)

  st.session_state.dom_content = cleaned_content

  with st.expander("Scraped Content"):
    st.text_area('scraped content',cleaned_content , height=300 )
     
