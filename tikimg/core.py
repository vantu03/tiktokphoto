import requests
from bs4 import BeautifulSoup

class TikTokPhoto:
    
    def __init__(
        self,
        url,
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile/15E148 Safari/604.1',
            'Accept-Language': 'en-US,en;q=0.9',
        },
        trys = 0
    ):
        self.input_url = url
        self.headers = headers
        self.result = []
        
    def extract_info(self, maxtrys=3):
        try:
            resp = requests.get(self.input_url, headers=self.headers, allow_redirects=True, timeout=10)
            resp.raise_for_status()
            
            match = re.search(r'/(video|photo)/(\d+)', resp.url)
            
            media_type = match.group(1)
            media_id = match.group(2)
            if media_id and media_type:
                
                resp = requests.get(f"https://www.tiktok.com/embed/v2/{media_id}", headers=self.headers, allow_redirects=True, timeout=10)
                resp.raise_for_status()
                
                if (media_type == 'photo'):
                    soup = BeautifulSoup(resp.text, "html.parser")
                
                    img_tags = soup.find_all("img")
    
                    for img in img_tags:
                        src = img.get("src")
                        if "Image" in img.get("alt") and src:
                            self.result.append(src)

        except Exception as e:
            pass

        return self.result