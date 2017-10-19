let bot = $('#bot_reply');
let msgDiv = $('.display-msgs');
let userInput = $('#userInput');
let chatBox = document.getElementById("box");

userInput.keypress((e) => {
    // Grab the `return` or `enter` keys
    let code = e.keyCode || e.which;
    // If the key `return` or `enter` is pressed
    if (code === 13) {
        let inp = userInput.val();
        let msg = {userMsg: inp};

        // append the inputted message to the chat area
        msgDiv.append('<div class="msg_bubble_user">' + inp + '</div>');
        // Auto scroll when messages exceed the height of the box
        chatBox.scrollTop = chatBox.scrollHeight;
        // clear user input
        userInput.val('');

        $.ajax({
            url: '/reply',
            type: 'POST',
            data: JSON.stringify(msg, null, 2),
            contentType: 'application/json;charset=UTF-8',
            success: (recvWeatherData) => {
                if (recvWeatherData.weather_data) {
                    fiveDayWeather(recvWeatherData)
                } else {
                    msgDiv.append('<div class="msg_bubble_bot right-align">'+ recvWeatherData.reply +'</div>');
                    chatBox.scrollTop = chatBox.scrollHeight;
                }
            },
            error: (err) => {
                console.log(err)
            }
        })
    }
});


function fiveDayWeather(weather) {
    // grab current temperature
    let curTemp = weather.weather_data.query.results.channel.item['condition'].temp;
    // grab condition description (i.e. sunny, cloudy)
    let cond = weather.weather_data.query.results.channel.item['condition']['text'];

    // 5 day forecast
    let fiveDayForecast = weather.five_day;
    // loop through array
    for (let i = 0; i < fiveDayForecast.length; i++) {
        console.log(`Text for today: ${fiveDayForecast[i]['text']}`)
    }

    // WeatherIcon.add('day1', WeatherIcon.SUN, {mode:WeatherIcon.DAY, stroke:true, shadow:true, animated:true});
    // WeatherIcon.add('day2', WeatherIcon.LIGHTRAINSUN, {mode:WeatherIcon.NIGHT, stroke:true, shadow:true, animated:true});
    // WeatherIcon.add('day3', WeatherIcon.LIGHTRAINTHUNDERSUN); // no parameters

    msgDiv.append('<div class="msg_bubble_bot right-align">'+ weather +'</div>');
    // Auto scroll when messages exceed the height of the box
    chatBox.scrollTop = chatBox.scrollHeight;
}