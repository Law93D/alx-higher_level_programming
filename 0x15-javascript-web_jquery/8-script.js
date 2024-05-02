// 8-script.js

$(document).ready(function () {
	$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
		data.results.forEach(function (movie) {
			$('<li>' + movie.title + '</li>').appendTo('#list_movies');
		});
	});
});
