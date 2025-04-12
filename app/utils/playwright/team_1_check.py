import os
from playwright.sync_api import sync_playwright

# Assuming you'll create these equivalent Python functions
# from utils.db.index_server import check_and_update_depth_chart, save_all_depth_charts
# from dao.index_server import depth_chart_create
# from dao.depth_chart_list_server import depth_chart_list_create


def team_1_check():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Get URL from environment variable
        page.goto(os.getenv("TEAM_1_URL"))
        
        page.set_viewport_size({"width": 1080, "height": 1024})
        
        # Get all table bodies
        tbodies = page.query_selector_all('table tbody')
        result = []
        
        # Process each tbody
        for tbody in tbodies:
            # Get all td elements in this tbody
            tds = tbody.query_selector_all('td')
            
            # Process each td
            for i in range(len(tds)):
                # Only process if index is at least 3 (to get preceding elements)
                if i >= 3:
                    # Check if current td has a link
                    link = tds[i].query_selector('a')
                    if link and link.get_attribute('href'):
                        # Get text from the three preceding cells
                        preceding_text = ', '.join([
                            tds[i-3].inner_text(),
                            tds[i-2].inner_text(),
                            tds[i-1].inner_text()
                        ])
                        
                        # Add to results
                        result.append({
                            "title": preceding_text,
                            "href": link.get_attribute('href')
                        })
        
        browser.close()
    

    # save_all_depth_charts(result=result, team_id=1, year=2024)
    
    #  trigger email

    return True