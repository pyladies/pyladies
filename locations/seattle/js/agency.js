/*!
* Start Bootstrap - Agency Bootstrap Theme (http://startbootstrap.com)
* Code licensed under the Apache License v2.0.
* For details, see http://www.apache.org/licenses/LICENSE-2.0.
*/

// jQuery for page scrolling feature - requires jQuery Easing plugin

$( document ).ready(function() {
  loadEventsFromMeetup();
  //loadEventsFromEventBrite();
});


function loadEventsFromMeetup() {
  var url = 'https://api.meetup.com/2/events?&sign=true&photo-host=public&group_urlname=seattle-pyladies&status=upcoming&page=12&key=5350685a4d783d675e4927440431a6c'

  // var url = 'https://api.meetup.com/events?&sign=true&photo-host=public&group_urlname=seattle-pyladies&page=20&key=5350685a4d783d675e4927440431a6c';

  $.ajax({ url: url,
    crossDomain: true,
    jsonp: "callback",
    dataType: "jsonp"
  }).success(function(data) {
    if (data.results.length == 0) {
      $('#no-events').html("No upcoming events scheduled.  Contact us to recommend a topic!");
    }else{
      console.log(data.results);


      for (i = 0; i < data.results.length; i++) {

        var date = new Date(data.results[i].time);

        var humanTime = date.toDateString()+ ' ' + '@'+ ' '+[(date.getHours() > 12 ? date.getHours() - 12 : date.getHours()),
          (date.getMinutes() == 0 ? "00" : date.getMinutes())
        ].join(':') + (date.getHours() > 12 ? " PM" : " AM");

        if (data.results[i].name.length > 25){
          var name =  data.results[i].name.substr(0,25)+"..."
        }
        else{
          var name =  data.results[i].name
        }


        $('.event-row').append('<div class="col-md-4 col-sm-6 events-item"> <a href="'+data.results[i].event_url+'" target=blank class="events-link"> <div class="events-caption"> <i class="fa fa-calendar fa-3x"></i> <h6>'+name+'</h6> <p class="text-muted">'+humanTime+'</p> <p> '+data.results[i].yes_rsvp_count+' pyladies attending</p> <div class="event-info">'+data.results[i].description+'</div> </div> </a> </div>')
      }

    }
  });
}

$(function() {
  $('a.page-scroll').bind('click', function(event) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: $($anchor.attr('href')).offset().top
    }, 1500, 'easeInOutExpo');
    event.preventDefault();
  });
});

// Highlight the top nav as scrolling occurs
$('body').scrollspy({
  target: '.navbar-fixed-top'
})

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
  $('.navbar-toggle:visible').click();
});
