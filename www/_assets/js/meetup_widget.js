/* Note: Updated to reflect JS Module pattern for encapsulation (v2)
 * To call: PyladiesMeetupWidget.addUpcomingMeetups(chapterIds)
 * Requests location meetups from Meetup.com coming up in the next month
 * and uses data to construct html entries for each event that are appended
 * to an '#upcomingMeetupsList' div in page's html.
 * Can be given any number of chapterIds.
 */

var PyladiesMeetupWidget = (function() {
  var key = '70704f53354b686770246f68494e2637';
  let aggResults = []
  // Private methods //

  _createEventUrls = function(url) {
    // creates <a href> links from urls for event clickthroughs
    return url
      .replace(/(ftp|http|https|file):\/\/[\S]+(\b|$)/gim, '"$&" target="_blank"')
      .replace(/([^\/])(www[\S]+(\b|$))/gim, '"https://$2" target="_blank"');
  };

  _createGroupUrl = function(group) {
    return 'https://meetup.com/' + group.urlname;
  };

  _convertMilisecondsToDate = function(ms) {
    // converts miliseconds since epoch to date format
    var date = new Date(ms);
    return String(date).slice(0, 11);
  };

  _getJSONMeetup = function(datum) {
    // {_buildHtml helper}
    // note: Not every meetup group event request returns a photo--not sure why, but
    // noticed that neither Taiwan or Bangalore's logos returned, so perhaps there
    // is some difference in data offered in parts of Asia?
    var json = {
      thumbLink: datum.group.group_photo ? datum.group.group_photo.thumb_link : "",
      groupName: datum.group.name,
      eventLink: datum.event_url ? _createEventUrls(datum.event_url) : _createGroupUrl(datum.group),
      eventName: datum.name,
      eventDate: _convertMilisecondsToDate(datum.time),
      sortDate: new Date(datum.time)
    };

    return json;
  };

  

  _getJSONTimepad = function(datum) {
    // {_buildHtml helper}
    // note: Not every meetup group event request returns a photo--not sure why, but
    // noticed that neither Taiwan or Bangalore's logos returned, so perhaps there
    // is some difference in data offered in parts of Asia?
    var json = {
      thumbLink: datum.poster_image.default_url ? datum.poster_image.default_url : "",
      groupName: datum.name,
      eventLink: datum.url ? _createEventUrls( datum.url ) : "",
      eventName: datum.name,
      eventDate: String(new Date(datum.starts_at)).slice(0,11),
      sortDate: new Date(datum.starts_at)
    };

    return json;
  };

  _processJsonResponse = function(data, processor){
    let processedJson = []
    for (var i = 0; i < data.length; i++) {
      datum = data[i];
      processedJson.push(processor(datum));
    }
    return processedJson;
  }

  //aggregate results from meetup.com and timepad, sort them by date
  _aggResults = function(data){
    aggResults = aggResults.concat(data)
    aggResults.sort(function(a,b){
      return new Date(a.sortDate) - new Date(b.sortDate);
    })
  }

  _makeAjaxRequest = function(ids, pages) {
    // fetch data
    $.ajax({
      url: 'https://api.meetup.com/2/events.json?key=' + key + '&group_id=' + ids +
        '&fields=group_photo&time=0m,1m&status=upcoming&sign=true&limited_events=true',
      dataType: 'jsonp',
      success: function(data) {
        return _aggResults(_processJsonResponse(data.results, _getJSONMeetup));
      },
      error: function(data) {
        _handleError(data);
      }
    }).then(function(){
        return $.ajax({
          url: 'https://api.timepad.ru/v1/events.json?organization_ids=' + pages,
          dataType: 'json',
          success: function(data) {
            _aggResults(_processJsonResponse(data.values, _getJSONTimepad));
          },
          error: function(data) {
             _handleError(data);
            if(meetup_data){
              print(meetup_data)
              return meetup_data;
          }
        }
      });
    }
  ).then(function(){
    _buildHtml(aggResults)
  })
};
  
  _buildHtml = function(data) {
    var html;

    // remove any old meetup list still attached to dom and append new $ul
    $('#upcomingMeetupsList ul').remove();
    $('#upcomingMeetupsList').append('<ul></ul>');

    for (var i = 0; i < data.length; i++) {
      datum = data[i];
      // todo(fw): pull this out into a template
      html = '<img class="meetup_group_icon" src="' + datum.thumbLink + '" height="80" width="80" />';
      html += '<p class="meetup_listing_group">' + datum.groupName + '</p>';
      html += '<p class="meetup_listing_event_title"><a href=' + datum.eventLink + '>' + datum.eventName + '</a></p>';
      html += '<p class="meetup_event_date">' + datum.eventDate + '</p>';

      $('#upcomingMeetupsList ul').append('<li>' + html + '</li>');
    }
  };

  _handleError = function(data) {
    // remove any stale list attached to dom and print error message
    $('#upcomingMeetupsList ul').remove();
    $('#upcomingMeetupsList')
      .append('<ul><li>Sorry, we are unable to reach Meetup.com at this time</li></ul>');
  };

  return {
    // returns public method
    addUpcomingMeetups: function(chapterIds, timePadPages) {
      console.log(timePadPages)
      _makeAjaxRequest(chapterIds, timePadPages);
    }
  };
})();
