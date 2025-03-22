from megascrapper import MegaScraper

# Initialize the scraper
scraper = MegaScraper()

# login_success = scraper.handle_login(
#     login_url="https://github.com/login",
#     credentials={"username": "ahammadnafiz", "password": "password"},
#     username_field={"type": "id", "value": "login_field"},
#     password_field={"type": "name", "value": "password"},
#     submit_button={"type": "xpath", "value": "//input[@name='commit']"}
# )

# if not login_success:
#     print("Login failed!")
#     exit()

# Infinite scrolling example

# Initialize the scraper
scraper = MegaScraper(
    headless=False,  # Set to True if you don't need to see the browser
    random_delay=True  # Add random delays for other actions too
)

try:
    # Start the browser
    scraper.start_browser()
    
    # Navigate to a website with infinite scrolling (using your example)
    scraper.navigate_to("https://unsplash.com/t/architecture-interior")
    
    # Define what data we want to extract
    extraction_config = {
        "image_urls": {
            "type": "css",
            "value": "figure a img",
            "attribute": "src",
            "multiple": True
        },
        "image_descriptions": {
            "type": "css",
            "value": "figure figcaption h4",
            "attribute": "text",
            "multiple": True
        },
        "photographer_names": {
            "type": "css",
            "value": "figure figcaption a[rel='nofollow']",
            "attribute": "text",
            "multiple": True
        }
    }
    
    # Perform the natural infinite scrolling and extract data
    results = scraper.infinite_scroll(
        max_scroll_time=30.0,  # Scroll for up to 90 seconds
        max_no_change_count=8,  # Stop after 8 scrolls with no new content
        extraction_config=extraction_config
    )
    
    # Process and save the extracted data
    # Flatten the results from multiple scrolls into one collection
    all_images = []
    for scroll_data in results:
        for i in range(len(scroll_data["image_urls"])):
            try:
                image_info = {
                    "url": scroll_data["image_urls"][i],
                    "description": scroll_data["image_descriptions"][i] if i < len(scroll_data["image_descriptions"]) else "",
                    "photographer": scroll_data["photographer_names"][i] if i < len(scroll_data["photographer_names"]) else ""
                }
                all_images.append(image_info)
            except IndexError:
                continue
    
    # Remove duplicates (by URL)
    seen_urls = set()
    unique_images = []
    for image in all_images:
        if image["url"] not in seen_urls:
            seen_urls.add(image["url"])
            unique_images.append(image)
    
    # Save the results
    scraper.save_data(unique_images, format="json", filename="unsplash_architecture")
    
    print(f"Collected {len(unique_images)} unique images")
    
finally:
    # Always close the browser when done
    scraper.close_browser()