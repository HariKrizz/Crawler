console.log("Hello");

function main() {
    $.get({url: 'http://127.0.0.1:5000/artist', success: (data) => {

        artist_list = "";
        data.forEach(i =>{ artist_list += `<li class="artist-item" data-id=${i.id}> ${i.name} </li>`; });

        html_tag = `<ol> ${artist_list} </ol>`;
        $("div.artistlist").html(html_tag);
        console.log(data);
        },   
    });

    $(document).on('click', 'li.artist-item', function () {
        artist_id = ($(this).data('id'));

        $.get({url:`http://127.0.0.1:5000/songs/${artist_id}`, success: (data)=>{
            song_list = "";
            data.forEach(i =>{song_list += `<li class="song-item" data-id=${i.song_id}> ${i.song_name} </li>`});
            html_tag = `<ol> ${song_list} </ol>`;
            $("div.songlist").html(html_tag);
            console.log(data);
            },  
        });
    });

    $(document).on('click', 'li.song-item', function () {
        song_id = $(this).data('id');
        $.get({url:`http://127.0.0.1:5000/songs/lyrics/${song_id}`, success: (data)=> {
            html_tag = `<pre> ${data[0]} </pre>`;
            $("div.songlyrics").html(html_tag);
            console.log(data);
            },  
        });
    }); 
}
$(main);