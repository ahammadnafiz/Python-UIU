### **Structural Tags**
- `<html>` – The root element of an HTML page.
- `<head>` – Contains metadata, title, and links to styles/scripts.
- `<body>` – Contains the main content of the webpage.
- `<div>` – A generic container used for grouping content.
- `<span>` – A small inline container, useful for styling parts of text.

### **Content Tags**
- `<h1>` to `<h6>` – Headings (h1 is the largest, h6 is the smallest).
- `<p>` – Paragraphs.
- `<a>` – Anchor tag for links (`href` attribute stores the URL).
- `<img>` – Images (`src` attribute stores the image URL).
- `<ul>` / `<ol>` – Unordered and ordered lists.
- `<li>` – List items (inside `<ul>` or `<ol>`).
- `<table>` – Defines a table.
  - `<tr>` – Table row.
  - `<td>` – Table cell.
  - `<th>` – Table header cell.
- `<form>` – Forms for user input.
  - `<input>` – Various types of input fields (`type="text"`, `type="password"`, `type="submit"`, etc.).
  - `<button>` – A clickable button.
  - `<textarea>` – Multi-line text input.
  - `<select>` / `<option>` – Dropdown menus.

### **Metadata & Script Tags**
- `<meta>` – Provides metadata (like character encoding, viewport settings).
- `<title>` – Page title (appears in the browser tab).
- `<link>` – Links to external stylesheets.
- `<script>` – Embeds JavaScript code or links to external scripts.

### **Common Tags for Web Scraping**
In **BeautifulSoup**, you'll frequently work with:
- **Links** (`<a>`): Extract URLs using `.find_all('a')` and `get('href')`.
- **Images** (`<img>`): Extract image sources using `.find_all('img')` and `get('src')`.
- **Tables** (`<table>`): Scrape structured data.
- **Divs with classes** (`<div class="example">`): Use `.find_all('div', class_="example")` to extract specific sections.
- **Paragraphs & Text** (`<p>`): Extract text content.


 # All major methods in BeautifulSoup (bs4)

## **1. Searching for Elements**
### **`find()`** - Finds the **first** matching element.
```python
soup.find("a")  # Finds the first <a> tag
soup.find("div", class_="content")  # Finds the first <div> with class "content"
```

### **`find_all()`** - Finds **all** matching elements (returns a list).
```python
soup.find_all("p")  # Finds all <p> tags
soup.find_all("a", limit=5)  # Finds the first 5 <a> tags
```

### **`select_one()`** - Finds the **first** matching CSS selector.
```python
soup.select_one("div.content p")  # Finds first <p> inside a <div class="content">
```

### **`select()`** - Finds **all** matching CSS selectors (returns a list).
```python
soup.select("div.content p")  # Finds all <p> inside <div class="content">
```

---

## **2. Navigating the HTML Structure**
### **Accessing Direct Elements**
#### **`soup.tag_name`** – Gets the first matching tag.
```python
soup.title  # <title> tag
soup.head  # <head> tag
soup.body  # <body> tag
```

### **`find_parent()`** - Finds the **closest parent** of an element.
```python
soup.find("span").find_parent("div")  # Finds the closest <div> containing a <span>
```

### **`find_parents()`** - Finds **all parent elements**.
```python
soup.find("span").find_parents()
```

### **`find_next_sibling()`** - Finds the **next sibling** of an element.
```python
soup.find("h2").find_next_sibling()  # Finds the next tag after <h2>
```

### **`find_previous_sibling()`** - Finds the **previous sibling** of an element.
```python
soup.find("h2").find_previous_sibling()
```

### **`find_next_siblings()`** - Finds **all next siblings**.
```python
soup.find("h2").find_next_siblings()
```

### **`find_previous_siblings()`** - Finds **all previous siblings**.
```python
soup.find("h2").find_previous_siblings()
```

---

## **3. Extracting Text & Attributes**
### **`.text` or `.get_text()`** - Extracts the text inside a tag.
```python
soup.find("p").text  # Extracts text from <p>
soup.find("p").get_text(strip=True)  # Removes extra spaces
```

### **`.string`** - Extracts text **if there's only one child**.
```python
soup.title.string  # Extracts text inside <title>
```

### **`.get()`** - Extracts a tag’s attribute (like `href`, `src`).
```python
soup.find("a").get("href")  # Extracts href from <a>
soup.find("img").get("src")  # Extracts image source
```

### **`.attrs`** - Returns all attributes of a tag as a dictionary.
```python
soup.find("a").attrs  # {'href': 'https://example.com', 'class': 'link'}
```

---

## **4. Modifying HTML (Not commonly used in scraping)**
### **`.decompose()`** - Removes a tag from the HTML.
```python
soup.find("script").decompose()  # Deletes <script> tags
```

### **`.replace_with()`** - Replaces a tag with new content.
```python
soup.find("span").replace_with("New text")
```

---

## **5. Working with HTML Documents**
### **`.prettify()`** - Formats and beautifies HTML.
```python
print(soup.prettify())  # Prints nicely formatted HTML
```

### **`.encode()`** - Converts soup object to bytes (useful for saving).
```python
html_bytes = soup.encode("utf-8")
```

---

## **6. Searching with Regular Expressions**
You can use `re` (regular expressions) for advanced searching.

```python
import re
soup.find_all("a", href=re.compile("example"))  # Finds all <a> tags with "example" in href
```

---

## **7. Handling Special Elements**
### **Finding comments**
```python
from bs4 import Comment
soup.find_all(string=lambda text: isinstance(text, Comment))
```

### **Finding elements with `data-attributes`**
```python
soup.find("div", {"data-id": "12345"})
```

---

## **Most Useful Combinations for Web Scraping**
### **Extracting all links**
```python
for link in soup.find_all("a"):
    print(link.get("href"))
```

### **Extracting all images**
```python
for img in soup.find_all("img"):
    print(img.get("src"))
```

### **Extracting table data**
```python
for row in soup.find("table").find_all("tr"):
    columns = row.find_all("td")
    data = [col.text.strip() for col in columns]
    print(data)
```

---
