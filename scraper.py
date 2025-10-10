import re

from playwright.sync_api import sync_playwright

from config import logger


def scrape_url_links() -> tuple[list[str], str]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        logger.info("Browser initiated.")

        # Open the website
        page.goto("https://www.kaufland.bg/broshuri.html")

        # Accept cookie popup
        logger.info("Accepting cookie popup")
        try:
            page.click("#onetrust-accept-btn-handler", timeout=5000)
        except Exception:
            logger.error("Error accepting cookie")
            raise Exception("Error accepting cookie")

        page.wait_for_timeout(2000)


        # Click on "Предстоящи събития"
        logger.info("Click on div")
        page.click("div:text(' Предстоящи предложения')")

        page.wait_for_timeout(2000)

        logger.info("Scrape dates")
        dates_els = page.query_selector_all("p.m-flyer-tile__validity-date")
        dates_el = dates_els[3]
        dates = dates_el.inner_text()

        
        tiles = page.query_selector_all("div.o-slider-to-grid__tile")
        fourth_tile = tiles[3]
        fourth_tile.click()

        # Accept cookie popup again if it appears
        logger.info("Click on brochure")
        try:
            page.click("#onetrust-accept-btn-handler", timeout=5000)
        except Exception:
            logger.error("Error on click on brochure")
            raise Exception("Error on click on brochure")

        img_links: list[str] = []

        while True:
            # Extract image links on current page
            logger.info("Start to extract images")
            images = page.query_selector_all(
                "li.page--current:not(.page--next):not(.page--pre) img.img"
            )

            for img in images:
                src = img.get_attribute("src")
                if src:
                    img_links.append(src)

            # Check stepper numbers
            stepper_text = page.inner_text("button.stepper--kaufland")
            match = re.match(r"(\d+)\s*/\s*(\d+)", stepper_text)
            if match:
                current, total = int(match.group(1)), int(match.group(2))
                if current == total:
                    break

            # Click next button
            try:
                page.click(
                    "button.button.button--primary-negative.button--label-uppercase.button--bold.button--icon.button--center.button--hover-background.button--navigation.button--navigation-kaufland[aria-label='Следваща страница']",
                    timeout=5000,
                )
            except Exception:
                logger.error("Error on click on next button")
                break

            page.wait_for_timeout(3000)

        logger.info("Collected image links:")
       
        logger.info(len(img_links))

        browser.close()

    logger.info("End of scraping")
    return img_links, dates
