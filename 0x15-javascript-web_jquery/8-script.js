$.getJSON( 'https://swapi.co/api/films/?format=json', function (data) {
  for (let a = 0; a < data.count; a++){
    $('UL#list_movies').append('<li>' + data.results[a].title + '</li>');
  }
});
