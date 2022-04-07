console.log("Hello");

function main() {
    $.get({url: 'http://127.0.0.1:5000/artist', success: (data) =>
        {
        artist_list = "";
        data.forEach(i =>{artist_list += '<li class="list-box">' +i.name+ '</li>';});

        html_tag = `<ul> ${artist_list} </ul>`;
        $("div.artistlist").html(html_tag);
        console.log(data);
        },   
    });
}

$(main);


