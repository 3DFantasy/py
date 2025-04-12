import os
from playwright.sync_api import sync_playwright

# Import the equivalent function from your Python module
# from utils.index_server import save_all_depth_charts

def team_7_check():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Get URL from environment variable
        page.goto(os.getenv("TEAM_7_URL"))
        
        page.set_viewport_size({"width": 1080, "height": 1024})
        
        # Get all table bodies
        tbodies = page.query_selector_all('table tbody')
        result = []
        
        # Process each tbody
        for tbody in tbodies:
            # Get all rows in this tbody
            rows = tbody.query_selector_all('tr')
            
            # Process each row
            for row in rows:
                # Get all cells in this row
                cells = row.query_selector_all('td')
                
                # Ensure there are at least four columns in the row
                if len(cells) >= 4:
                    # Get the text from the first column
                    text = cells[0].inner_text()
                    
                    # Get the href from the fourth column
                    link = cells[3].query_selector('a')
                    if link and link.get_attribute('href'):
                        # Add the result to the array only if a valid href is found
                        result.append({
                            "title": text,
                            "href": link.get_attribute('href')
                        })
        
        browser.close()
    
    # save_all_depth_charts(result=result, team_id=7, year=2024)

    # trigger email

    
    return True