///Asks Meetup.com for any public event listing from one of the PyLadies chapters upcoming in the next week

//helper functions
function create_urls(input) {
        return input
        .replace(/(ftp|http|https|file):\/\/[\S]+(\b|$)/gim, '"$&" target="_blank"')
        .replace(/([^\/])(www[\S]+(\b|$))/gim, '"http://$2" target="_blank"');
} //end url parsing helper

function convert_time_miliseconds_to_date(t) {
        var d = new Date(t); // The 0 there is the key, which sets the date to the epoch
        return String(d).slice(0, 11);
} //end convert miliseconds_to_date

// functions
function addUpcomingMeetups() {
   // meetup group_ids in order: portland, san francisco, la, nyc, dc, atlanta, seattle, austin, brno/cz, san diego, toronto
   var chapter_ids = '4808882,3604052,2288171,4576312,2292131,4507652,5411282,5947662,5160912,5089102,6488102';
   var meetup_key = '70704f53354b686770246f68494e2637';

   $.ajax( {
       url: 'http://api.meetup.com/2/events.json?key='+meetup_key+'&group_id='+chapter_ids+'&fields=group_photo&time=0m,1m&status=upcoming&sign=true',
       dataType: 'jsonp',
       success: function(data) {
          buildHtml(data);
       }, //end success
       error: function(data) {
          handleError(data);
       } //end error
     }); //end .ajax()
     return false;
} //end addUpcomingMeetups function

function buildHtml(data) {
    $('#upcomingMeetupsList ul').remove();
    $('#upcomingMeetupsList').append('<ul></ul>');
    for (var key in data.results) {
      url_link = create_urls(data.results[key].event_url);
      event_date = convert_time_miliseconds_to_date(data.results[key].time);
      var html = '<img class="meetup_group_icon" src="'+data.results[key].group.group_photo.thumb_link+'" height="80" width="80" />';
      html += '<p class="meetup_listing_group">'+data.results[key].group.name+'</p>';
      html += '<p class="meetup_listing_event_title"><a href='+url_link+'>'+data.results[key].name+'</a></p>';
      html += '<p class="meetup_event_date">'+event_date+'</p>';
      $('#upcomingMeetupsList').find('ul').append('<li>'+html+'</li>');
    }
}

function handleError(data) {
    $('#upcomingMeetupsList ul').remove();
    $('#upcomingMeetupsList').append('<ul></ul>');
    $('#upcomingMeetupsList').find('ul').append('<li>Sorry, we are unable to reach Meetup.com at this time</li>');
}
