# scripts/fetch_youtube.py
import urllib.request
import xml.etree.ElementTree as ET
import json

CHANNEL_ID = 'UClRZ_X9qhqv14H53-g9qfrQ'
RSS_URL = f'https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}'

def fetch_videos():
    try:
        # Загружаем XML
        with urllib.request.urlopen(RSS_URL, timeout=30) as response:
            xml_data = response.read()
        
        root = ET.fromstring(xml_data)
        
        # Пространства имен в XML YouTube
        ns = {
            'atom': 'http://www.w3.org/2005/Atom',
            'yt': 'http://www.youtube.com/xml/schemas/2015'
        }
        
        videos = []
        for entry in root.findall('atom:entry', ns):
            title = entry.find('atom:title', ns).text
            link = entry.find('atom:link', ns).attrib['href']
            video_id = entry.find('yt:videoId', ns).text
            
            videos.append({
                'title': title,
                'link': link,
                'videoId': video_id
            })
            
            # Берем только 7 последних видео
            if len(videos) >= 7:
                break
        
        # Сохраняем в JSON
        with open('youtube-videos.json', 'w', encoding='utf-8') as f:
            json.dump(videos, f, ensure_ascii=False, indent=2)
            
        print(f"Успешно сохранено {len(videos)} видео.")
        
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")

if __name__ == '__main__':
    fetch_videos()