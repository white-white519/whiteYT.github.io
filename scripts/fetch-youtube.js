const fs = require('fs');
const fetch = require('node-fetch'); // Потребуется установить

const YT_CHANNEL_ID = 'UClRZ_X9qhqv14H53-g9qfrQ';
const RSS_URL = `https://www.youtube.com/feeds/videos.xml?channel_id=${YT_CHANNEL_ID}`;

async function fetchVideos() {
    try {
        const response = await fetch(RSS_URL);
        const xml = await response.text();

        // Простой парсинг XML (можно использовать библиотеку, но для примера так)
        const videoRegex = /<entry>[\s\S]*?<title>(.*?)<\/title>[\s\S]*?<link rel="alternate" href="(.*?)"\/>[\s\S]*?<\/entry>/g;
        const videos = [];
        let match;

        while ((match = videoRegex.exec(xml)) !== null) {
            videos.push({
                title: match[1],
                link: match[2]
            });
        }

        fs.writeFileSync('youtube.json', JSON.stringify(videos.slice(0, 7)));
        console.log('youtube.json обновлён!');
    } catch (error) {
        console.error('Ошибка:', error);
    }
}

fetchVideos();