function add_content(data){
    if(data['Response']=="True")
    {
        document.getElementById('error_message').style.display = "none";
        document.getElementById('movie_info').style.display = "inline-block";
        document.getElementById('poster').src= data['Poster'];
        document.getElementById('title').innerHTML= data['Title'];
        document.getElementById('release').innerHTML= data['Released'];
        document.getElementById('rated').innerHTML= data['Rated'];
        document.getElementById('runtime').innerHTML= data['Runtime'];
        document.getElementById('genre').innerHTML= data['Genre'];
        document.getElementById('plot').innerHTML= data['Plot'];
    }
    else
    {
        document.getElementById('movie_info').style.display="none";
        document.getElementById('error_message').style.display = "inline-block";
    }
}
function search()
{
    let search = document.getElementById('search-text').value;
    fetch('http://www.omdbapi.com/?apikey=56439a3c&t=' + search)
    .then(function(response)
    {
            return response.json();
    })
    .then(add_content);
}