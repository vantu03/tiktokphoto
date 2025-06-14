# TikTokPhoto

> A simple Python tool to extract photo mode image URLs from TikTok posts.

**TikTokPhoto** is a lightweight Python class that extracts image links from TikTok photo posts by scraping the public embed page — no API keys or login required.

---

## Features

- Get all photo URLs from TikTok "photo mode"
- Uses mobile headers (iPhone) for better TikTok compatibility
- No TikTok API, cookies, or login needed
- Fast and minimal

---

## File Structure

```

tiktokphoto/
├── core.py          # Main logic containing TikTokPhoto class
├── README.md        # Project readme
└── ...

````

---

## Quick Start

### Install dependencies

```bash
pip install requests beautifulsoup4
````

### Usage

```python
from core import TikTokPhoto

url = 'https://www.tiktok.com/@tiktokphotomodejp/photo/7210615980077108481'
extractor = TikTokPhoto(url)
images = extractor.extract_info()

for i, img in enumerate(images, 1):
    print(f"Image {i}: {img}")
```

### Sample Output

```
Image 1: https://p16-sign-sg.tiktokcdn.com/tos-alisg-i-photomode-sg/xxx...
Image 2: https://p16-sign-sg.tiktokcdn.com/tos-alisg-i-photomode-sg/yyy...
...
```

---

## How It Works

1. Extracts TikTok ID from the given post URL.
2. Requests TikTok's embed endpoint (e.g., `https://www.tiktok.com/embed/v2/{id}`).
3. Parses image `<img>` tags with `alt="Image"` to extract valid URLs.

---

## Class Reference

```python
class TikTokPhoto:
    def __init__(self, url: str, headers: dict = None, trys: int = 0):
        # Initialize with TikTok URL

    def extract_info(self, maxtrys: int = 3) -> list:
        # Return list of image URLs
```

---

## Requirements

* Python 3.7+
* `requests`
* `beautifulsoup4`

---

## License

[MIT License](LICENSE)

---

## Author

Made by [vantu03](https://github.com/vantu03)

> PRs and stars are welcome
