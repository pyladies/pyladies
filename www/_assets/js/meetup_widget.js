/* Note: Updated to reflect JS Module pattern for encapsulation (v2)
 * To call: PyladiesMeetupWidget.addUpcomingMeetups(chapterIds)
 * Requests location meetups from Meetup.com coming up in the next month
 * and uses data to construct html entries for each event that are appended
 * to an '#upcomingMeetupsList' div in page's html.
 * Can be given any number of chapterIds.
 */

var PyladiesMeetupWidget = (function() {
  var key = '70704f53354b686770246f68494e2637';

  // Private methods //

  _createEventUrls = function(url) {
    // creates <a href> links from urls for event clickthroughs
    return url
      .replace(/(ftp|http|https|file):\/\/[\S]+(\b|$)/gim, '"$&" target="_blank"')
      .replace(/([^\/])(www[\S]+(\b|$))/gim, '"http://$2" target="_blank"');
  };

  _createGroupUrl = function(group) {
    return 'http://meetup.com/' + group.urlname;
  };

  _convertMilisecondsToDate = function(ms) {
    // converts miliseconds since epoch to date format
    var date = new Date(ms);
    return String(date).slice(0, 11);
  };

  _makeAjaxRequest = function(ids) {
    // fetch data
    $.ajax({
      url: 'http://api.meetup.com/2/events.json?key=' + key + '&group_id=' + ids +
        '&fields=group_photo&time=0m,1m&status=upcoming&sign=true&limited_events=true',
      dataType: 'jsonp',
      success: function(data) {
        _buildHtml(data);
      },
      error: function(data) {
        _handleError(data);
      }
    });
  };

  _getJSON = function(datum) {
    // {_buildHtml helper}
    // note: Not every meetup group event request returns a photo--not sure why, but
    // noticed that neither Taiwan or Bangalore's logos returned, so perhaps there
    // is some difference in data offered in parts of Asia?
    var json = {
      thumbLink: datum.group.group_photo ? datum.group.group_photo.thumb_link : "",
      groupName: datum.group.name,
      eventLink: datum.event_url ? _createEventUrls(datum.event_url) : _createGroupUrl(datum.group),
      eventName: datum.name,
      eventDate: _convertMilisecondsToDate(datum.time)
    };

    return json;
  };

  _buildHtml = function(data) {
    var html;
    var datum;
    var json;

    // remove any old meetup list still attached to dom and append new $ul
    $('#upcomingMeetupsList ul').remove();
    $('#upcomingMeetupsList').append('<ul></ul>');

    for (var i = 0; i < data.results.length; i++) {
      datum = data.results[i];
      json = _getJSON(datum);

      // todo(fw): pull this out into a template
      html = '<img class="meetup_group_icon" src="' + json.thumbLink + '" height="80" width="80" />';
      html += '<p class="meetup_listing_group">' + json.groupName + '</p>';
      html += '<p class="meetup_listing_event_title"><a href=' + json.eventLink + '>' + json.eventName + '</a></p>';
      html += '<p class="meetup_event_date">' + json.eventDate + '</p>';

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
    addUpcomingMeetups: function(chapterIds) {
      _makeAjaxRequest(chapterIds);
    }
  };
})();