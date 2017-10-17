let btn = $('#btn');
let bot = $('#bot_reply');

btn.click(() => {
    let inp = $('#userInput').val();
    let msg = {userMsg: inp};

    $.ajax({
        url: '/reply',
        type: 'POST',
        data: JSON.stringify(msg, null, 2),
        contentType: 'application/json;charset=UTF-8',
        success: (recvWeatherData) => {
            if (recvWeatherData.weather_data) {
                fiveDayWeather(recvWeatherData)
            } else {
                bot.text(recvWeatherData.reply);
            }
        },
        error: (err) => {
            console.log(err)
        }
    })
});


function fiveDayWeather(weather) {
    // 5 day forecast
    let fiveDay = weather.weather_data['query']['results']['channel']['item']['forecast'];
    // loop through array
    for (let i = 0; i < fiveDay.length; i++) {
        console.log(`High today: ${fiveDay[i].high}`)
    }
    // grab current temperature
    let curTemp = weather.weather_data.query.results.channel.item['condition'].temp;
    // grab condition description (i.e. sunny, cloudy)
    let cond = weather.weather_data.query.results.channel.item['condition']['text'];

    WeatherIcon.add('day1', WeatherIcon.SUN, {mode:WeatherIcon.DAY, stroke:true, shadow:true, animated:true});
    WeatherIcon.add('day2', WeatherIcon.LIGHTRAINSUN, {mode:WeatherIcon.NIGHT, stroke:true, shadow:true, animated:true});
    WeatherIcon.add('day3', WeatherIcon.LIGHTRAINTHUNDERSUN); // no parameters

    bot.text(weather);
}