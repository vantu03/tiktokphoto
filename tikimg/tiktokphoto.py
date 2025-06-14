import requests
from bs4 import BeautifulSoup
import re
import json

class TikTokExtractor:
    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X)',
            'Accept-Language': 'en-US,en;q=0.9',
        }

    def extract(self):
        result = {
            "title": None,
            "author": None,
            "thumbnail": None,
            "photos": [],
            "audios": []
        }

        try:
            # B1: Lấy URL thực
            resp = requests.get(self.url, headers=self.headers, timeout=10, allow_redirects=True)
            resp.raise_for_status()
            final_url = resp.url

            match = re.search(r'/(video|photo)/(\d+)', final_url)
            if not match:
                return None

            media_type = match.group(1)
            media_id = match.group(2)

            if media_type != 'photo':
                return None

            # B2: Truy cập trang embed
            embed_url = f"https://www.tiktok.com/embed/v2/{media_id}"
            resp = requests.get(embed_url, headers=self.headers, timeout=10)
            resp.raise_for_status()
            
            soup = BeautifulSoup(resp.text, "html.parser")
            div_tag = soup.find("div")
            if div_tag:
                result["title"] = div_tag.get_text(strip=True)
    
            audio_tags = soup.find_all("audio")
            for audio in audio_tags:
                src = audio.get("src")
                if src:
                    result["audios"].append(src)
            
            img_tags = soup.find_all("img")
            for img in img_tags:
                src = img.get("src")
                if "Image" in (img.get("alt") or "") and src:
                    result["photos"].append(src)

            if result["photos"]:
                result["thumbnail"] = result["photos"][0]
            
        except Exception as e:
            return None

        return result
