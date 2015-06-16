///Asks Meetup.com for any public event listing from one of the PyLadies chapters upcoming in the next week
//Localized for use by any chapter--just copy file over to your location site and sub your meetup key for "meetup_key" and meetup group id (indicated as data id on locations index.html page) for "chapter_ids" in addUpcomingMeetups function.

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
function addUpcomingMeetups(chapter_ids) {
   var meetup_key = '5b2055f1f7f7b522f405f479365b2';

   $.ajax( {
       url: 'http://api.meetup.com/2/events.json?key='+meetup_key+'&group_id='+chapter_ids+'&time=0m,3m&status=upcoming&sign=true',
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
    for (var key in data.results) {
      url_link = create_urls(data.results[key].event_url);
      event_date = convert_time_miliseconds_to_date(data.results[key].time);
      var html = '<dd class="meetup_event_date">'+event_date+'</dd>' + '<dt><a href='+url_link+'>'+data.results[key].name+'</a></dt>';
      html += '<dd class="meetup_event_venue">'+data.results[key].venue.name+', ';
      html += data.results[key].venue.city+', '+data.results[key].venue.state+'</dd>';
      html += '<dd class="meetup_event_description">'+data.results[key].description+'</dd>';
      $('#upcomingMeetupsList').append('<dl>'+html+'</dl>');
    }
}

function handleError(data) {
    $('#upcomingMeetupsList ul').remove();
    $('#upcomingMeetupsList').append('<ul></ul>');
    $('#upcomingMeetupsList').find('ul').append('<li>Sorry, we are unable to reach Meetup.com at this time</li>');
}
