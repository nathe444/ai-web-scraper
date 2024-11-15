# AI Web Scraper

An intelligent web scraping application that uses AI to extract and analyze content from websites.

## Features

- Web scraping using Selenium and BeautifulSoup4
- AI-powered content analysis using Groq
- Interactive UI with Streamlit
- Natural language querying of scraped content

## Prerequisites

- Python 3.8+
- Chrome browser
- ChromeDriver
- Groq API key

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download ChromeDriver:
   - Visit [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/#stable)
   - Download the ChromeDriver version that matches your Chrome browser version
   - Extract the downloaded file and place `chromedriver.exe` in the project root directory

4. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

## Usage

1. Start the application:
   ```bash
   streamlit run main.py
   ```

2. Enter a URL to scrape
3. Wait for the scraping to complete
4. Enter your query to analyze the scraped content
5. View the AI-generated results

## Project Structure

- `main.py`: Main Streamlit application
- `scraper.py`: Web scraping functionality
- `parser.py`: AI content parsing using Groq
- `requirements.txt`: Project dependencies

## Notes

- Ensure your Chrome browser version matches the ChromeDriver version
- The application requires an active internet connection
- Large websites may take longer to scrape
- API rate limits may apply when using Groq