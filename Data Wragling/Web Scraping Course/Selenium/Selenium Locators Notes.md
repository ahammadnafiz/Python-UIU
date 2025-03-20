## **🔹 1. By ID**
**Best for:** When an element has a unique `id`.  
✅ **Fastest and most reliable.**

### **Example: Locating a Login Button**
🔍 **HTML**
```html
<button id="login-btn">Login</button>
```
💻 **Selenium Code**
```python
driver.find_element(By.ID, "login-btn").click()
```
---

## **🔹 2. By Name**
**Best for:** Input fields with a `name` attribute.  
✅ **Good alternative to ID.**

### **Example: Google Search Box**
🔍 **HTML**
```html
<input type="text" name="q">
```
💻 **Selenium Code**
```python
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)
```
---

## **🔹 3. By Class Name**
**Best for:** Elements with a `class` name.  
🚨 **Not unique? Use XPath instead.**

### **Example: Find a Search Button**
🔍 **HTML**
```html
<button class="search-btn">Search</button>
```
💻 **Selenium Code**
```python
driver.find_element(By.CLASS_NAME, "search-btn").click()
```
---

## **🔹 4. By Tag Name**
**Best for:** Finding multiple elements like `<a>`, `<button>`, `<img>`.  
🔹 **Used for scraping and automation.**

### **Example: Get All Links on a Page**
```python
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text, "->", link.get_attribute("href"))
```
---

## **🔹 5. By CSS Selector**
**Best for:** Short and flexible element selection.  
✅ **Faster than XPath.**

### **Example: Find a Button in a Div**
🔍 **HTML**
```html
<div class="container">
    <button id="signup-btn">Sign Up</button>
</div>
```
💻 **Selenium Code**
```python
driver.find_element(By.CSS_SELECTOR, "div.container button").click()
```
✔ **CSS Selector Syntax:**
- `#id` → `driver.find_element(By.CSS_SELECTOR, "#login-btn")`
- `.class` → `driver.find_element(By.CSS_SELECTOR, ".search-btn")`
- `tagname[attr=value]` → `driver.find_element(By.CSS_SELECTOR, "input[name='q']")`
- `parent child` → `driver.find_element(By.CSS_SELECTOR, "div.container button")`
---

## **🔹 6. By XPath**
**Best for:** Dynamic elements and deeply nested elements.  
🚀 **Slower than CSS selectors, but more powerful.**

### **Example: Amazon Search Box**
🔍 **HTML**
```html
<input type="text" id="twotabsearchtextbox">
```
💻 **Selenium Code**
```python
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Laptop")
```
✔ **XPath Syntax:**
- **Exact Match:** `//tagname[@attribute='value']`
  ```python
  driver.find_element(By.XPATH, "//input[@name='q']")
  ```
- **Contains:** `//tagname[contains(@attribute, 'partial-value')]`
  ```python
  driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
  ```
- **Text Match:** `//tagname[text()='Exact Text']`
  ```python
  driver.find_element(By.XPATH, "//h1[text()='Welcome']").click()
  ```
- **Following Sibling:** `//tagname[@attribute='value']/following-sibling::tagname`
  ```python
  driver.find_element(By.XPATH, "//label[@for='username']/following-sibling::input").send_keys("user123")
  ```

---

## **🔹 7. By Link Text**
**Best for:** Clicking on **exact** text inside an `<a>` tag.

### **Example: Clicking the "Contact Us" Link**
🔍 **HTML**
```html
<a href="/contact">Contact Us</a>
```
💻 **Selenium Code**
```python
driver.find_element(By.LINK_TEXT, "Contact Us").click()
```
---

## **🔹 8. By Partial Link Text**
**Best for:** Clicking on **part of** a link text.

### **Example: Click "Read More" Link**
🔍 **HTML**
```html
<a href="/blog/post-123">Read More about Selenium</a>
```
💻 **Selenium Code**
```python
driver.find_element(By.PARTIAL_LINK_TEXT, "Read More").click()
```
✔ **Even if the text is long, Selenium will still find it!**

---

### **📌 Summary of Selenium Locators**
| Locator | Syntax | Use Case |
|---------|--------|----------|
| **By ID** | `By.ID, "login-btn"` | Unique elements like buttons |
| **By Name** | `By.NAME, "q"` | Form inputs (e.g., search bars) |
| **By Class Name** | `By.CLASS_NAME, "search-btn"` | Buttons, labels with class attributes |
| **By Tag Name** | `By.TAG_NAME, "a"` | Multiple elements (e.g., all links) |
| **By CSS Selector** | `By.CSS_SELECTOR, "div.container button"` | Fast and flexible selection |
| **By XPath** | `By.XPATH, "//input[@id='search']"` | Dynamic elements, nested elements |
| **By Link Text** | `By.LINK_TEXT, "Contact Us"` | Clicking on full link text |
| **By Partial Link Text** | `By.PARTIAL_LINK_TEXT, "Read More"` | Clicking on part of a link |

---

### **💡 Best Practices**
✔ **Use `By.ID` whenever possible** (fastest).  
✔ **Prefer `By.CSS_SELECTOR` over `By.XPATH`** (faster).  
✔ **Use `By.XPATH` for dynamic elements**.  
✔ **Avoid `By.CLASS_NAME` if the class is common**.  
✔ **Use `By.LINK_TEXT` for navigation links**.