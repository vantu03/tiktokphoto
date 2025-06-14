# TikTokExtractor

TikTokExtractor là một thư viện Python đơn giản giúp trích xuất ảnh, âm thanh, tiêu đề, tác giả và ảnh đại diện từ các bài viết TikTok dạng video hoặc chế độ ảnh.

Không cần đăng nhập, không dùng API, hoạt động bằng cách phân tích trang nhúng công khai của TikTok.

---

## Tính năng

- Trích xuất URL ảnh từ bài viết TikTok ở chế độ ảnh (photo mode)
- Lấy liên kết âm thanh (audio) nếu có
- Lấy tiêu đề, tên người đăng và ảnh đại diện (thumbnail)
- Không cần API, cookie hay đăng nhập

---

## Cấu trúc thư mục

```

tiktokextractor/
├── core.py          # Chứa class TikTokExtractor
├── README.md        # Tài liệu dự án

````

---

## Cài đặt

```bash
pip install requests beautifulsoup4
````

---

## Sử dụng

```python
from core import TikTokExtractor

url = 'https://www.tiktok.com/@tiktokphotomodejp/photo/7210615980077108481'
extractor = TikTokExtractor(url)
info = extractor.extract()

print("Tiêu đề:", info["title"])
print("Tác giả:", info["author"])
print("Thumbnail:", info["thumbnail"])

print("Ảnh:")
for photo in info["photos"]:
    print(" -", photo)

print("Âm thanh:")
for audio in info["audios"]:
    print(" -", audio)
```

---

## Ví dụ đầu ra

```
Tiêu đề: Mèo dễ thương trên TikTok
Tác giả: tiktokphotomodejp
Thumbnail: https://p16-sign-sg.tiktokcdn.com/...

Ảnh:
 - https://p16-sign-sg.tiktokcdn.com/...
 - https://p16-sign-sg.tiktokcdn.com/...

Âm thanh:
 - https://sf16-ies-music.tiktokcdn.com/...
```

---

## Cách hoạt động

1. Phân tích URL để lấy ID TikTok từ đường dẫn.
2. Gửi yêu cầu đến trang nhúng công khai của TikTok (`/embed/v2/{id}`).
3. Sử dụng BeautifulSoup để phân tích HTML, tìm ảnh, âm thanh và thông tin metadata.

---

## Tài liệu class

```python
class TikTokExtractor:
    def __init__(self, url: str, headers: dict = None):
        # Khởi tạo với URL TikTok

    def extract(self) -> dict:
        # Trả về dict gồm:
        # {
        #   "title": str | None,
        #   "author": str | None,
        #   "thumbnail": str | None,
        #   "photos": List[str],
        #   "audios": List[str]
        # }
```

---

## Yêu cầu

* Python 3.7 trở lên
* `requests`
* `beautifulsoup4`

---

## Tác giả

Tạo bởi [vantu03](https://github.com/vantu03)

Bạn có thể đóng góp bằng cách mở pull request hoặc tạo issue.