# filename: selenium_mcp_server.py

from mcp.server import Server
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize MCP server
server = Server("selenium-mcp")

# Global driver (for simplicity, start Chrome once)
driver = webdriver.Chrome()

# Tool: Open a URL
@server.tool()
def open_url(url: str) -> str:
    driver.get(url)
    return f"Opened {url}"

# Tool: Click element by CSS selector
@server.tool()
def click(selector: str) -> str:
    element = driver.find_element(By.CSS_SELECTOR, selector)
    element.click()
    return f"Clicked element {selector}"

# Tool: Type into element
@server.tool()
def type_text(selector: str, text: str) -> str:
    element = driver.find_element(By.CSS_SELECTOR, selector)
    element.send_keys(text)
    return f"Typed '{text}' into {selector}"

# Tool: Get text from element
@server.tool()
def get_text(selector: str) -> str:
    element = driver.find_element(By.CSS_SELECTOR, selector)
    return element.text

if __name__ == "__main__":
    server.run()