import aiohttp


class WeatherCollector:

    async def collect_weather_data(self):
        async with aiohttp.ClientSession() as session:
            url = "https://api.open-meteo.com/v1/forecast?latitude=55.6878&longitude=37.3684&current_weather=true"
            async with session.get(url) as response:
                data = await response.json()
                weather = data["current_weather"]
        return weather


