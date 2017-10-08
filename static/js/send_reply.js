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
            bot.text(resp.reply);
        },
        error: (err) => {
            console.log(err)
        }
    })
});