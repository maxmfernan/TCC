$(document).ready(function() {
	
	var options = {
		allow_empty: true,
		filters: [
			{
				id: "name",
				label: "Name",
				type: "string",
				default_value: "Max",
				size: 30,
				unique: true
			}
		]
	};


	$('#q-builder').queryBuilder(options);

	$('.parse-json').on('click', function() {
		console.log(JSON.stringify(
			$('#builder').queryBuilder('getRules'),
			undefined, 2
		));
	});


});  