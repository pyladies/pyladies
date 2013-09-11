$(document).ready(function(){
	init();
});

var theData;

function init() {
	Tabletop.init( { key: '0AmUutu5ZyTjPdHFma0FycVF5X0dTb090blIxNEVNU0E',
	callback: function(data) {  
		theData = data;
			
	    $('#library').dataTable( {
        "aaData": theData,
        "aoColumns": [
            { "mData": "title" },
            { "mData": "author" },
            { "mData": "publisher" },
            { "mData": "language" },
            { "mData": "level" },
            { "mData": "description"},
            { "mData": "available"}
        ],
        "bAutoWidth": false,
        "bPaginate": false,
        "fnInitComplete": function(){
	        $("#libraryContainer").fadeIn(100);
        }
    } ); 
    
	 },
	simpleSheet: true } );
/* 	$("#libraryContainer").hide().delay(200).fadeIn(); */
}