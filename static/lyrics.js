console.log("Hello");

function main() {
    $.get({url: 'http://127.0.0.1:5000/api/artist', success: (data) => {

        artist_list = "";
        data.forEach(i =>{ artist_list += `<li class="artist-item" data-id=${i.id} data-name=${i.name}> ${i.name} </li>`; });

        html_tag = `<h4 class=artist><b>Artists<b></h4><hr><ul type="none"> ${artist_list} </ul>`;
        $("div.artistlist").html(html_tag);
        console.log(data);
        },   
    });

    $(document).on('click', 'li.artist-item', function () {

        artist_id = ($(this).data('id'));
        artist_name = ($(this).data('name'));
        
        $.get({url:`http://127.0.0.1:5000/api/songs/${artist_id}`, success: (data)=>{
            song_list = "";
            data.forEach(i =>{song_list += `<li class="song-item" data-id=${i.song_id}> ${i.song_name} </li>`});
            html_tag = `<h4 class=songs><b>Songs<b></h4><hr><ul type="none"> ${song_list} </ol>`;
            $("div.songlist").html(html_tag);
            console.log(data);
            },  
        });
    });

    $(document).on('click', 'li.song-item', function () {
        song_id = $(this).data('id');
        $.get({url:`http://127.0.0.1:5000/api/songs/lyrics/${song_id}`, success: (data)=> {
            html_tag = `<h4 class=lyric_heading><b>Lyrics<b></h4><hr>
            <h3 class =lyric_heading><b>${data[1]}<b></h3><hr><br> <pre><b>${data[0]}<b></pre>`;
            $("div.songlyrics").html(html_tag);
            console.log(data);
            },  
        });
    }); 
}
$(main);