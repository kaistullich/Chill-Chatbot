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
        success: (resp) => {
            if (resp.weather_data) {
                // console.log(resp);
                // grab current temperature
                let curTemp = resp.weather_data.query.results.channel.item['condition'].temp;
                // grab condition description (i.e. sunny, cloudy)
                let cond = resp.weather_data.query.results.channel.item['condition']['text'];
                bot.text(resp)
            } else {
                bot.text(resp.reply);
            }
        },
        error: (err) => {
            console.log(err)
        }
    })
});