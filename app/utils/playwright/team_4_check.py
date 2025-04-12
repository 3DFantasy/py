#  SAME AS TEAM 2
import os
from playwright.sync_api import sync_playwright

# Import the equivalent function from your Python module
# from utils.index_server import save_all_depth_charts


def team_4_check():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get URL from environment variable
        page.goto(os.getenv("TEAM_4_URL"))

        page.set_viewport_size({"width": 1080, "height": 1024})

        # Get all table bodies
        tbodies = page.query_selector_all("table tbody")
        result = []

        # Process each tbody
        for tbody in tbodies:
            # Get all rows in this tbody
            rows = tbody.query_selector_all("tr")

            # Process each row
            for row in rows:
                # Get all cells in this row
                cells = row.query_selector_all("td")

                # Only process if there are at least 5 cells
                if len(cells) >= 5:
                    # Get text from the first three cells
                    text = ", ".join(
                        [
                            cells[0].inner_text(),
                            cells[1].inner_text(),
                            cells[2].inner_text(),
                        ]
                    )

                    # Check if the 5th cell has a link
                    link = cells[4].query_selector("a")
                    if link and link.get_attribute("href"):
                        # Add to results
                        result.append(
                            {"title": text, "href": link.get_attribute("href")}
                        )

        browser.close()

    # save_all_depth_charts(result=result, team_id=4, year=2024)

    #  trigger email

    return True
