"""
Example usage of Stealthium package.

StealthChrome is a drop-in replacement for webdriver.Chrome.
Use it exactly like Selenium, but with additional stealth features.
"""

import logging
from stealthium import StealthChrome, StealthSession

# Setup logging (optional)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def example_basic_usage():
    """Example: Use StealthChrome exactly like webdriver.Chrome."""
    print("\n=== Example 1: Basic Usage (Just like Selenium) ===")
    
    # Create driver - works exactly like webdriver.Chrome()
    driver = StealthChrome(headless=True)
    
    try:
        # Use it exactly like Selenium
        driver.get('https://example.com')
        print(f"Page Title: {driver.title}")
        print(f"Page URL: {driver.current_url}")
        
        # All Selenium methods work
        element = driver.find_element('tag name', 'h1')
        print(f"Found element: {element.text}")
        
    finally:
        driver.quit()


def example_with_headers():
    """Example: Extract headers from browser."""
    print("\n=== Example 2: Extract Headers ===")
    
    driver = StealthChrome(headless=True)
    
    try:
        driver.get('https://httpbin.org/headers')
        
        # Extract headers - this is a new method not in standard Selenium
        headers = driver.get_headers()
        print(f"User-Agent: {headers.get('user-agent', 'Not found')}")
        print(f"Accept: {headers.get('accept', 'Not found')}")
        
    finally:
        driver.quit()


def example_with_proxy():
    """Example: Use proxy (set during initialization)."""
    print("\n=== Example 3: Using Proxy ===")
    
    # Set proxy when creating the driver
    # Uncomment and add your proxy details:
    # driver = StealthChrome(
    #     headless=True,
    #     proxy_host='your-proxy-host.com',
    #     proxy_port=8080,
    #     proxy_user='username',  # Optional
    #     proxy_password='password'  # Optional
    # )
    # 
    # try:
    #     driver.get('https://httpbin.org/ip')
    #     print(f"IP Response: {driver.page_source}")
    # finally:
    #     driver.quit()
    
    print("(Proxy example commented out - add your proxy details to test)")


def example_selenium_compatibility():
    """Example: Demonstrates full Selenium compatibility."""
    print("\n=== Example 4: Full Selenium Compatibility ===")
    
    driver = StealthChrome(headless=True)
    
    try:
        driver.get('https://example.com')
        
        # All standard Selenium methods work:
        print(f"Current URL: {driver.current_url}")
        print(f"Page Source Length: {len(driver.page_source)}")
        
        # Find elements
        elements = driver.find_elements('tag name', 'p')
        print(f"Found {len(elements)} paragraph elements")
        
        # Execute JavaScript
        result = driver.execute_script("return document.title;")
        print(f"Title via JavaScript: {result}")
        
        # Get cookies
        cookies = driver.get_cookies()
        print(f"Cookies: {len(cookies)} found")
        
    finally:
        driver.quit()


def example_context_manager():
    """Example: Using context manager."""
    print("\n=== Example 5: Context Manager ===")
    
    # Use with statement for automatic cleanup
    with StealthChrome(headless=True) as driver:
        driver.get('https://example.com')
        print(f"Page Title: {driver.title}")
        # Driver automatically quits when exiting the context


def example_custom_options():
    """Example: Using custom ChromeOptions."""
    print("\n=== Example 6: Custom Options ===")
    
    from selenium.webdriver.chrome.options import Options
    import time
    
    # Create custom options
    options = Options()
    options.add_argument('--window-size=1920,1080')
    
    # Pass to StealthChrome (stealth features will still be applied)
    driver = StealthChrome(options=options, headless=False, incognito=True)
    
    try:
        driver.get('https://google.com')
        size = driver.get_window_size()
        print(f"Window Size: {size['width']}x{size['height']}")
        time.sleep(60)
    finally:
        driver.quit()
    


if __name__ == "__main__":
    try:
        # example_basic_usage()
        # example_with_headers()
        # example_with_proxy()
        # example_selenium_compatibility()
        # example_context_manager()
        # example_custom_options()
        example_custom_options()
        
        print("\n✅ All examples completed!")
        print("\nStealthChrome works exactly like webdriver.Chrome!")
        print("Just replace 'webdriver.Chrome()' with 'StealthChrome()'")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
