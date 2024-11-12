import streamlit as st
from scraper import scrape_website, extract_body_content, clean_body_content, split_dom_content
from parser import parse_with_groq


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
     

if "dom_content" in st.session_state:
  query = st.text_area("Enter your query:")

  if st.button("Search"):
    if query:
      st.write("Searching...")
      
      dom_chunks = split_dom_content(st.session_state.dom_content)

      result = parse_with_groq(dom_chunks , query)
      st.write(result)