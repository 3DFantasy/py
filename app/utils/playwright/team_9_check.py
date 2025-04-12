# SAME AS TEAM 8
import os
from playwright.sync_api import sync_playwright

# # Import the equivalent function from your Python module
# from utils.index_server import save_all_depth_charts


def team_9_check():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get URL from environment variable
        page.goto(os.getenv("TEAM_9_URL"))

        page.set_viewport_size({"width": 1080, "height": 1024})

        # Extract hrefs from <td> tags with <a> elements
        result = []

        # Get all table bodies
        tbodies = page.query_selector_all("table tbody")

        for tbody in tbodies:
            # Get all td elements in this tbody
            tds = tbody.query_selector_all("td")

            # Process each td
            for index, td in enumerate(tds):
                # Look for links in the td
                link = td.query_selector("a")

                # If we found a link and we're at least at the 4th td (index >= 3)
                if link and link.get_attribute("href") and index >= 3:
                    # Get the text from the three preceding td elements
                    preceding_text = ", ".join(
                        [
                            tds[index - 3].inner_text(),
                            tds[index - 2].inner_text(),
                            tds[index - 1].inner_text(),
                        ]
                    )

                    # Add to results
                    result.append(
                        {"title": preceding_text, "href": link.get_attribute("href")}
                    )

        browser.close()

    # save_all_depth_charts(result=result, team_id=9, year=2024)

    # trigger email

    return True
