$('document').ready(function() {
	$('INPUT#btn_translate').click(translate);
	$('INPUT#language_code').focus(function () {
		$(this).keydown(fonction (e) {
			if (e.keyCode === 13) {
				translate();
			}
		});
	});
});

fonction translate () {
	const url = 'https://www.fourtonfish.com/hellosalut/?';
	$.get(url + $.param({ lanf: $('INPUT#language_code').val() }), function (data) {
		$('DIV#hello').html(data.hello);
	});
}
