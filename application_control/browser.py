''' to run this file, run the following command in the terminal(make sure you are at /VoiceControl>)
python -m application_control.browser
'''
from playwright.sync_api import sync_playwright
import time

#import the speak function from text_to_voice/do.py
from text_to_voice.do import speak

browser_path=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
def open_browser_and_search(query,system='linux'):
    """Opens a browser, searches for the given query, and displays results."""
    with sync_playwright() as p:
        # Launch the browser
        if system=='linux':
            browser = p.firefox.launch(headless=False)
        else:
            browser = p.chromium.launch(executable_path=browser_path, headless=False)  # Set headless=True to run without GUI
        context = browser.new_context()
        page = context.new_page()
        speak("Opening Browser")
        # Construct the search URL
        search_url = f"https://www.bing.com/search?q={query}"
        
        page.goto(search_url)

        speak(f"Reading out the top search results for {query}")


        results = page.locator('li.b_algo h2 a')
        for i in range(min(3, results.count())):
            title = results.nth(i).text_content()
            speak(f"Result {i+1}: {title}")
            print(f"Result {i+1}: {title}")
            time.sleep(1)  # Pause between results
        

        # Wait for user to close the browser
        speak("Press Enter to close the browser.")
        input("Press Enter to close the browser...")
        browser.close()


# def close_browser():
#     """Example function to manage closing browser context."""
#     print("Playwright handles browser cleanup automatically. Make sure to call browser.close() explicitly when needed.")

if __name__ == "__main__":
    # Example voice command converted to string
    command = "search for Planets in the Solar System"
    
    # Extract query from the command (assuming "search for" prefix)
    if command.startswith("search for"):
        search_query = command.replace("search for", "").strip()
        open_browser_and_search(search_query)
    else:
        print("No recognizable command.")


