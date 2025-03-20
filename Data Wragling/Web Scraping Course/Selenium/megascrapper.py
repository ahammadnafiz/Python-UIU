import time
import json
import random
import logging
import argparse
from typing import Dict, List, Optional, Union, Any
import csv
import os
from urllib.parse import urlparse

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, 
    NoSuchElementException, 
    ElementClickInterceptedException,
    StaleElementReferenceException,
    WebDriverException
)
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("scraper.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("MegaScraper")

class MegaScraper:
    """A versatile web scraper that can bypass various protection mechanisms."""
    
    def __init__(
        self, 
        headless: bool = False, 
        proxy: Optional[str] = None,
        user_agent: Optional[str] = None,
        timeout: int = 30,
        wait_time: int = 10,
        random_delay: bool = True,
        min_delay: float = 0.5,
        max_delay: float = 3.0
    ):
        """
        Initialize the MegaScraper with customizable options.
        
        Args:
            headless: Run browser in headless mode
            proxy: Optional proxy server (format: "ip:port")
            user_agent: Custom user agent string
            timeout: Default timeout for page loads and element waits
            wait_time: Default explicit wait time
            random_delay: Add random delays between actions to appear more human-like
            min_delay: Minimum delay in seconds
            max_delay: Maximum delay in seconds
        """
        self.headless = headless
        self.proxy = proxy
        self.user_agent = user_agent or self._get_random_user_agent()
        self.timeout = timeout
        self.wait_time = wait_time
        self.random_delay = random_delay
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.driver = None
        self.wait = None
        self.session_cookies = {}
        
    def _get_random_user_agent(self) -> str:
        """Return a random modern user agent string."""
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1"
        ]
        return random.choice(user_agents)
    
    def start_browser(self) -> None:
        """Initialize and start the browser with configured options."""
        options = Options()
        
        if self.headless:
            options.add_argument("--headless=new")
        
        # Add common options to help bypass protections
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument(f"user-agent={self.user_agent}")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        
        # Add proxy if specified
        if self.proxy:
            options.add_argument(f"--proxy-server={self.proxy}")
        
        # Initialize the WebDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        # self.driver = uc.Chrome(options=options)
        
        # Set window size to a common resolution
        self.driver.set_window_size(1920, 1080)
        
        # Apply additional stealth techniques
        self._apply_stealth_techniques()
        
        # Create wait object
        self.wait = WebDriverWait(self.driver, self.wait_time)
        
        logger.info("Browser started successfully")
    
    def _apply_stealth_techniques(self) -> None:
        """Apply advanced stealth techniques to avoid detection."""
        # Execute JavaScript to modify navigator properties
        if self.driver:
            self.driver.execute_script("""
                // Overwrite the 'webdriver' property
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => false
                });
                
                // Create a fake plugins array
                const makePluginArray = () => {
                    const plugins = [
                        {name: 'Chrome PDF Plugin', filename: 'internal-pdf-viewer'},
                        {name: 'Chrome PDF Viewer', filename: 'mhjfbmdgcfjbbpaeojofohoefgiehjai'},
                        {name: 'Native Client', filename: 'internal-nacl-plugin'}
                    ];
                    const pluginArray = plugins.map(plugin => {
                        const pluginObj = {};
                        pluginObj.name = plugin.name;
                        pluginObj.filename = plugin.filename;
                        pluginObj.description = '';
                        pluginObj.version = '';
                        return pluginObj;
                    });
                    
                    // Mock plugins array
                    pluginArray.__proto__ = plugins.__proto__;
                    return pluginArray;
                };
                
                // Apply the fake plugins
                if (navigator.plugins.length === 0) {
                    Object.defineProperty(navigator, 'plugins', {
                        get: () => makePluginArray()
                    });
                }
                
                // Add a fake language list
                Object.defineProperty(navigator, 'languages', {
                    get: () => ['en-US', 'en']
                });
                
                // Mock the permissions API
                if (!window.Notification) {
                    window.Notification = {
                        permission: 'default'
                    };
                }
            """)
            logger.debug("Applied stealth techniques")
    
    def human_like_delay(self) -> None:
        """Add a random delay to simulate human behavior if enabled."""
        if self.random_delay:
            delay = random.uniform(self.min_delay, self.max_delay)
            time.sleep(delay)
    
    def navigate_to(self, url: str) -> bool:
        """
        Navigate to a URL with error handling.
        
        Args:
            url: The URL to navigate to
            
        Returns:
            bool: True if navigation was successful, False otherwise
        """
        if not self.driver:
            self.start_browser()
        
        try:
            logger.info(f"Navigating to: {url}")
            self.driver.get(url)
            self.human_like_delay()
            
            # Wait for page to load
            self.driver.execute_script("return document.readyState === 'complete'")
            
            # Store cookies in session
            self._update_session_cookies()
            
            # Handle common overlay/popup scenarios
            self._handle_common_overlays()
            
            return True
        except WebDriverException as e:
            logger.error(f"Failed to navigate to {url}: {str(e)}")
            return False
    
    def _update_session_cookies(self) -> None:
        """Update internal cookie storage."""
        if self.driver:
            cookies = self.driver.get_cookies()
            for cookie in cookies:
                self.session_cookies[cookie['name']] = cookie['value']
    
    def _handle_common_overlays(self) -> None:
        """Handle common overlay patterns like cookie notices, newsletter popups, etc."""
        if not self.driver:
            return
            
        # List of common overlay selectors and close button patterns
        overlay_patterns = [
            # Cookie consent patterns
            {"type": "id", "pattern": "cookie-banner", "close_pattern": "//button[contains(text(), 'Accept') or contains(text(), 'Close') or contains(text(), 'Got it')]"},
            {"type": "id", "pattern": "gdpr", "close_pattern": "//button[contains(text(), 'Accept') or contains(text(), 'Close')]"},
            {"type": "id", "pattern": "consent", "close_pattern": "//button[contains(text(), 'Accept') or contains(text(), 'I agree')]"},
            
            # Newsletter/subscription popups
            {"type": "class", "pattern": "newsletter", "close_pattern": "//button[contains(@class, 'close') or contains(text(), 'No thanks')]"},
            {"type": "class", "pattern": "popup", "close_pattern": "//div[contains(@class, 'close') or contains(@class, 'dismiss')]"},
            
            # Generic modals
            {"type": "class", "pattern": "modal", "close_pattern": "//button[contains(@class, 'close')]"},
        ]
        
        # Try each pattern
        for pattern in overlay_patterns:
            try:
                # Check if the overlay exists
                if pattern["type"] == "id":
                    element = self.driver.find_element(By.ID, pattern["pattern"])
                elif pattern["type"] == "class":
                    element = self.driver.find_element(By.CLASS_NAME, pattern["pattern"])
                else:
                    continue
                    
                # If overlay found, try to close it
                if element and element.is_displayed():
                    try:
                        # Try to find and click the close button
                        close_button = self.driver.find_element(By.XPATH, pattern["close_pattern"])
                        if close_button and close_button.is_displayed():
                            close_button.click()
                            self.human_like_delay()
                            logger.debug(f"Closed overlay with pattern: {pattern['pattern']}")
                    except (NoSuchElementException, ElementClickInterceptedException):
                        # If can't find specific close button, try ESC key
                        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                        self.human_like_delay()
            except NoSuchElementException:
                # This pattern not found, continue to next
                continue
            except Exception as e:
                logger.debug(f"Error handling overlay: {str(e)}")
                continue
    
    def wait_for_element(
        self, 
        locator_type: str, 
        locator_value: str, 
        timeout: Optional[int] = None,
        condition: str = "presence"
    ) -> Optional[webdriver.remote.webelement.WebElement]:
        """
        Wait for an element to be available according to the specified condition.
        
        Args:
            locator_type: Type of locator (id, class, css, xpath, etc.)
            locator_value: Value of the locator
            timeout: Custom timeout (uses default if None)
            condition: Type of wait condition ('presence', 'visibility', 'clickable')
            
        Returns:
            WebElement if found, None otherwise
        """
        if not self.driver:
            logger.error("Driver not initialized. Call start_browser() first.")
            return None
            
        timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, timeout)
        
        by_type = self._get_by_type(locator_type)
        
        try:
            if condition == "visibility":
                element = wait.until(EC.visibility_of_element_located((by_type, locator_value)))
            elif condition == "clickable":
                element = wait.until(EC.element_to_be_clickable((by_type, locator_value)))
            else:  # Default to presence
                element = wait.until(EC.presence_of_element_located((by_type, locator_value)))
            
            self.human_like_delay()
            return element
        except TimeoutException:
            logger.warning(f"Timed out waiting for element: {locator_type}={locator_value}")
            return None
        except Exception as e:
            logger.error(f"Error waiting for element: {str(e)}")
            return None
    
    def _get_by_type(self, locator_type: str) -> str:
        """Convert string locator type to Selenium By type."""
        locator_map = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "css": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "link": By.LINK_TEXT,
            "partial_link": By.PARTIAL_LINK_TEXT,
            "tag": By.TAG_NAME
        }
        
        return locator_map.get(locator_type.lower(), By.CSS_SELECTOR)
    
    def find_elements(
        self, 
        locator_type: str, 
        locator_value: str
    ) -> List[webdriver.remote.webelement.WebElement]:
        """
        Find all elements matching the given locator.
        
        Args:
            locator_type: Type of locator (id, class, css, xpath, etc.)
            locator_value: Value of the locator
            
        Returns:
            List of WebElements
        """
        if not self.driver:
            logger.error("Driver not initialized. Call start_browser() first.")
            return []
            
        by_type = self._get_by_type(locator_type)
        
        try:
            elements = self.driver.find_elements(by_type, locator_value)
            return elements
        except Exception as e:
            logger.error(f"Error finding elements: {str(e)}")
            return []
    
    def scroll_to_bottom(self, incremental: bool = True, scroll_pause_time: float = 1.0) -> None:
        """
        Scroll to the bottom of the page, either incrementally or all at once.
        
        Args:
            incremental: If True, scroll in increments. If False, scroll directly to bottom.
            scroll_pause_time: Time to pause between scrolls when incremental is True
        """
        if not self.driver:
            logger.error("Driver not initialized. Call start_browser() first.")
            return
            
        if incremental:
            # Get scroll height
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            
            while True:
                # Scroll down incrementally
                self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
                
                # Wait for content to load
                time.sleep(scroll_pause_time)
                
                # Calculate new scroll height and compare with last scroll height
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    # If heights are the same, we've reached the bottom
                    break
                last_height = new_height
        else:
            # Scroll directly to the bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
    
    def click_element(
        self, 
        element: Union[webdriver.remote.webelement.WebElement, Dict[str, str]], 
        js_click: bool = False,
        retry: int = 3
    ) -> bool:
        """
        Click on an element with multiple fallback methods.
        
        Args:
            element: WebElement object or dict with 'type' and 'value' keys
            js_click: If True, use JavaScript to click instead of Selenium
            retry: Number of retry attempts
            
        Returns:
            bool: True if click was successful, False otherwise
        """
        if not self.driver:
            logger.error("Driver not initialized. Call start_browser() first.")
            return False
            
        # Convert dictionary to WebElement if needed
        if isinstance(element, dict) and 'type' in element and 'value' in element:
            try:
                target_element = self.wait_for_element(
                    element['type'], 
                    element['value'],
                    condition="clickable"
                )
            except Exception as e:
                logger.error(f"Error finding element to click: {str(e)}")
                return False
        else:
            target_element = element
        
        if not target_element:
            logger.warning("Element not found for clicking")
            return False
            
        for attempt in range(retry):
            try:
                # Scroll element into view
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_element)
                self.human_like_delay()
                
                if js_click:
                    # Click using JavaScript
                    self.driver.execute_script("arguments[0].click();", target_element)
                else:
                    # Regular Selenium click
                    target_element.click()
                
                self.human_like_delay()
                return True
            except ElementClickInterceptedException:
                # Something is blocking the click, try JavaScript click
                try:
                    self.driver.execute_script("arguments[0].click();", target_element)
                    self.human_like_delay()
                    return True
                except Exception as e:
                    logger.warning(f"JS click also failed: {str(e)}")
            except StaleElementReferenceException:
                # Element is stale, need to find it again
                if isinstance(element, dict) and 'type' in element and 'value' in element:
                    try:
                        target_element = self.wait_for_element(
                            element['type'], 
                            element['value'],
                            condition="clickable"
                        )
                        if not target_element:
                            logger.warning("Element became stale and couldn't be relocated")
                            return False
                    except Exception as e:
                        logger.error(f"Error relocating stale element: {str(e)}")
                        return False
                else:
                    # Can't relocate if we don't have the locator information
                    logger.warning("Element is stale and can't be relocated")
                    return False
            except Exception as e:
                logger.warning(f"Click failed (attempt {attempt+1}/{retry}): {str(e)}")
                
            # Wait before retry
            time.sleep(1)
        
        logger.error(f"Failed to click element after {retry} attempts")
        return False
    
    def fill_form(self, form_data: Dict[str, Any]) -> bool:
        """
        Fill a form with provided data.
        
        Args:
            form_data: Dictionary mapping of field locators to values
                Format: {
                    "field_name": {
                        "type": "locator_type", 
                        "value": "locator_value",
                        "data": "value_to_input"
                    },
                    ...
                }
                
        Returns:
            bool: True if form was filled successfully, False otherwise
        """
        if not self.driver:
            logger.error("Driver not initialized. Call start_browser() first.")
            return False
            
        success = True
        
        for field_name, field_info in form_data.items():
            try:
                locator_type = field_info.get("type", "id")
                locator_value = field_info.get("value", "")
                input_value = field_info.get("data", "")
                is_dropdown = field_info.get("is_dropdown", False)
                is_checkbox = field_info.get("is_checkbox", False)
                
                # Wait for the field to be visible
                field_element = self.wait_for_element(
                    locator_type, 
                    locator_value,
                    condition="visibility"
                )
                
                if not field_element:
                    logger.warning(f"Could not find form field: {field_name}")
                    success = False
                    continue
                
                # Handle different field types
                if is_dropdown:
                    # Handle dropdown selection
                    from selenium.webdriver.support.ui import Select
                    select = Select(field_element)
                    select.select_by_visible_text(input_value)
                elif is_checkbox:
                    # Handle checkbox
                    current_state = field_element.is_selected()
                    if (input_value and not current_state) or (not input_value and current_state):
                        self.click_element(field_element)
                else:
                    # Regular text input
                    field_element.clear()
                    # Type like a human - character by character with small delays
                    for char in input_value:
                        field_element.send_keys(char)
                        time.sleep(random.uniform(0.01, 0.1))
                
                self.human_like_delay()
                logger.debug(f"Successfully filled field: {field_name}")
            except Exception as e:
                logger.error(f"Error filling form field {field_name}: {str(e)}")
                success = False
        
        return success
    
    def extract_data(self, extraction_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract data from the current page according to the provided configuration.
        
        Args:
            extraction_config: Dictionary with extraction rules
                Format: {
                    "data_point_name": {
                        "type": "locator_type",
                        "value": "locator_value",
                        "attribute": "attribute_name",  # Optional, defaults to text
                        "multiple": False  # If True, returns a list of values
                    },
                    ...
                }
                
        Returns:
            Dictionary with extracted data
        """
        if not self.driver:
            logger.error("Driver not initialized. Call start_browser() first.")
            return {}
            
        results = {}
        
        for data_name, config in extraction_config.items():
            try:
                locator_type = config.get("type", "css")
                locator_value = config.get("value", "")
                attribute = config.get("attribute", "text")
                multiple = config.get("multiple", False)
                
                if multiple:
                    elements = self.find_elements(locator_type, locator_value)
                    if attribute == "text":
                        results[data_name] = [el.text.strip() for el in elements]
                    else:
                        results[data_name] = [el.get_attribute(attribute) for el in elements]
                else:
                    element = self.wait_for_element(locator_type, locator_value)
                    if element:
                        if attribute == "text":
                            results[data_name] = element.text.strip()
                        else:
                            results[data_name] = element.get_attribute(attribute)
                    else:
                        results[data_name] = None
            except Exception as e:
                logger.error(f"Error extracting {data_name}: {str(e)}")
                results[data_name] = None
        
        return results
    
    def paginate(
        self, 
        next_button: Dict[str, str],
        max_pages: int = 5,
        wait_time: float = 2.0,
        extraction_config: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        Navigate through paginated content and optionally extract data from each page.
        
        Args:
            next_button: Dictionary with "type" and "value" for the next button locator
            max_pages: Maximum number of pages to navigate
            wait_time: Time to wait after clicking next button
            extraction_config: Optional config for data extraction on each page
            
        Returns:
            List of dictionaries with extracted data if extraction_config is provided,
            otherwise an empty list
        """
        if not self.driver:
            logger.error("Driver not initialized. Call start_browser() first.")
            return []
            
        all_results = []
        
        for page in range(max_pages):
            logger.info(f"Processing page {page + 1}/{max_pages}")
            
            # Extract data from current page if extraction config is provided
            if extraction_config:
                page_data = self.extract_data(extraction_config)
                all_results.append(page_data)
            
            # Try to find and click the next button
            next_element = self.wait_for_element(
                next_button["type"],
                next_button["value"],
                condition="clickable"
            )
            
            if not next_element or not next_element.is_displayed():
                logger.info("No more pages to navigate")
                break
                
            # Check if next button is disabled
            disabled = next_element.get_attribute("disabled")
            aria_disabled = next_element.get_attribute("aria-disabled")
            if disabled or aria_disabled == "true":
                logger.info("Next button is disabled. End of pagination.")
                break
                
            # Click the next button
            success = self.click_element(next_element)
            if not success:
                logger.warning("Failed to click next button")
                break
                
            # Wait for the page to load
            time.sleep(wait_time)
            
            # Update session cookies
            self._update_session_cookies()
        
        return all_results
    
    def infinite_scroll(
        self, 
        scroll_pause_time: float = 1.0,
        max_scrolls: int = 10,
        extraction_config: Optional[Dict[str, Any]] = None,
        stop_condition: Optional[Dict[str, str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Handle infinite scrolling pages and optionally extract data.
        
        Args:
            scroll_pause_time: Time to pause between scrolls
            max_scrolls: Maximum number of scrolls to perform
            extraction_config: Optional config for data extraction after each scroll
            stop_condition: Optional dictionary with "type" and "value" for element that
                            indicates the end of scrolling
                            
        Returns:
            List of dictionaries with extracted data if extraction_config is provided,
            otherwise an empty list
        """
        if not self.driver:
            logger.error("Driver not initialized. Call start_browser() first.")
            return []
            
        all_results = []
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        
        for scroll_num in range(max_scrolls):
            logger.info(f"Scroll {scroll_num + 1}/{max_scrolls}")
            
            # Scroll down
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            
            # Check if we've reached the end of the page by height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            
            # Extract data if config is provided
            if extraction_config:
                page_data = self.extract_data(extraction_config)
                all_results.append(page_data)
            
            # Check for stop condition if provided
            if stop_condition:
                try:
                    stop_element = self.driver.find_element(
                        self._get_by_type(stop_condition["type"]),
                        stop_condition["value"]
                    )
                    if stop_element and stop_element.is_displayed():
                        logger.info("Stop condition element found. Ending infinite scroll.")
                        break
                except NoSuchElementException:
                    pass  # Stop element not found, continue scrolling
            
            # If we've reached the bottom of the page, break
            if new_height == last_height:
                logger.info("Reached the bottom of the page. No more content to load.")
                break
                
            last_height = new_height
        
        return all_results
    
    def handle_login(
        self, 
        login_url: str,
        credentials: Dict[str, str],
        username_field: Dict[str, str],
        password_field: Dict[str, str],
        submit_button: Dict[str, str],
        success_indicator: Optional[Dict[str, str]] = None,
        failure_indicator: Optional[Dict[str, str]] = None,
        captcha_handler: Optional[callable] = None
    ) -> bool:
        """
        Handle login process on websites.
        
        Args:
            login_url: URL of the login page
            credentials: Dictionary with "username" and "password" keys
            username_field: Dictionary with "type" and "value" for username field locator
            password_field: Dictionary with "type" and "value" for password field locator
            submit_button: Dictionary with "type" and "value" for submit button locator
            success_indicator: Optional dict with "type" and "value" for success indicator
            failure_indicator: Optional dict with "type" and "value" for failure indicator
            captcha_handler: Optional function to handle captchas
            
        Returns:
            bool: True if login was successful, False otherwise
        """
        if not self.driver:
            self.start_browser()
        
        # Navigate to login page
        if not self.navigate_to(login_url):
            logger.error("Failed to navigate to login page")
            return False
        
        # Fill login form
        form_data = {
            "username": {
                "type": username_field["type"],
                "value": username_field["value"],
                "data": credentials["username"]
            },
            "password": {
                "type": password_field["type"],
                "value": password_field["value"],
                "data": credentials["password"]
            }
        }
        
        if not self.fill_form(form_data):
            logger.error("Failed to fill login form")
            return False
        
        # Handle captcha if present and handler provided
        if captcha_handler:
            captcha_result = captcha_handler(self.driver)
            if not captcha_result:
                logger.error("Captcha handling failed")
                return False
        
        # Submit the form
        submit_element = self.wait_for_element(
            submit_button["type"],
            submit_button["value"],
            condition="clickable"
        )
        
        if not submit_element:
            logger.error("Submit button not found")
            return False
            
        if not self.click_element(submit_element):
            logger.error("Failed to click submit button")
            return False

        # Wait for login completion
        try:
            # Check for success or failure indicators
            success = False
            
            if success_indicator:
                success_element = self.wait_for_element(
                    success_indicator["type"],
                    success_indicator["value"],
                    timeout=30
                )
                if success_element:
                    logger.info("Login successful - success indicator found")
                    success = True
            else:
                # If no success indicator provided, check URL change
                current_url = self.driver.current_url
                if current_url != login_url:
                    logger.info("Login likely successful - URL changed")
                    success = True

            # Check for failure indicator even if success was detected
            if failure_indicator:
                failure_element = self.wait_for_element(
                    failure_indicator["type"],
                    failure_indicator["value"],
                    timeout=5
                )
                if failure_element:
                    logger.error("Login failed - failure indicator present")
                    success = False

            # Final verification through cookies
            if success and not any('session' in k.lower() for k in self.session_cookies):
                logger.warning("No session cookies detected after login")
                success = False

            self._update_session_cookies()
            return success

        except Exception as e:
            logger.error(f"Login verification failed: {str(e)}")
            return False
        
    def check_robots_txt(self, url: str):
        """Automated robots.txt compliance"""
        from urllib.robotparser import RobotFileParser
        rp = RobotFileParser()
        rp.set_url(urlparse(url).scheme + "://" + urlparse(url).netloc + "/robots.txt")
        rp.read()
        return rp.can_fetch(self.user_agent, url)
    
    def take_screenshot(self, element: WebElement = None):
        """Enhanced visual debugging"""
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.screenshot("element.png")
        else:
            self.driver.save_screenshot("fullpage.png")

    def download_file(self, element: WebElement, save_path: str):
        """Handle file downloads"""
        url = element.get_attribute("href")
        headers = {"User-Agent": self.user_agent}
        response = requests.get(url, headers=headers, stream=True)
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

    def add_middleware(self, middleware_type: str, callback: callable):
        """Plugin system for custom processing"""
        self.middleware.setdefault(middleware_type, []).append(callback)

    def _run_middleware(self, middleware_type: str, data: Any):
        """Execute middleware pipeline"""
        for middleware in self.middleware.get(middleware_type, []):
            data = middleware(data)
        return data

    def execute_ajax_request(self, script: str):
        """Direct AJAX handling"""
        return self.driver.execute_async_script(f"""
            var callback = arguments[arguments.length - 1];
            {script}.then(callback).catch(callback);
        """)

    def switch_to_iframe(self, identifier: Union[str, WebElement]):
        """Enhanced iframe handling"""
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(identifier))

    def close_browser(self) -> None:
        """Close the browser instance and cleanup resources."""
        if self.driver:
            try:
                self.driver.quit()
                logger.info("Browser closed successfully")
            except Exception as e:
                logger.error(f"Error closing browser: {str(e)}")
            finally:
                self.driver = None
                self.wait = None

    def save_data(
        self, 
        data: Union[Dict, List[Dict]], 
        format: str = "json",
        filename: str = "output"
    ) -> None:
        """
        Save extracted data to file.
        
        Args:
            data: Data to save
            format: Output format (json, csv, excel)
            filename: Base filename (without extension)
        """
        try:
            if format == "json":
                with open(f"{filename}.json", "w") as f:
                    json.dump(data, f, indent=2)
            elif format == "csv":
                if isinstance(data, list):
                    keys = data[0].keys()
                    with open(f"{filename}.csv", "w", newline="") as f:
                        writer = csv.DictWriter(f, fieldnames=keys)
                        writer.writeheader()
                        writer.writerows(data)
                else:
                    logger.error("CSV format requires list of dictionaries")
            elif format == "excel":
                df = pd.DataFrame(data)
                df.to_excel(f"{filename}.xlsx", index=False)
            else:
                logger.error(f"Unsupported format: {format}")
                return
                
            logger.info(f"Data saved to {filename}.{format}")
        except Exception as e:
            logger.error(f"Failed to save data: {str(e)}")

    def __del__(self):
        """Destructor to ensure browser is closed on object deletion."""
        self.close_browser()