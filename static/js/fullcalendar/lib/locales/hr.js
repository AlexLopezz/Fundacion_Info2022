FullCalendar.globalLocales.push(function () {
  'use strict';

  var hr = {
<<<<<<< HEAD
    code: 'hr',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 7, // The week that contains Jan 1st is the first week of the year.
    },
    buttonText: {
      prev: 'Prijašnji',
      next: 'Sljedeći',
      today: 'Danas',
      month: 'Mjesec',
      week: 'Tjedan',
      day: 'Dan',
      list: 'Raspored',
    },
    weekText: 'Tje',
    allDayText: 'Cijeli dan',
    moreLinkText: function(n) {
      return '+ još ' + n
    },
    noEventsText: 'Nema događaja za prikaz',
=======
    code: "hr",
    week: {
      dow: 1,
      doy: 7
    },
    buttonText: {
      prev: "Prija\u0161nji",
      next: "Sljede\u0107i",
      today: "Danas",
      month: "Mjesec",
      week: "Tjedan",
      day: "Dan",
      list: "Raspored"
    },
    weekText: "Tje",
    allDayText: "Cijeli dan",
    moreLinkText: function(n) {
      return "+ jo\u0161 " + n;
    },
    noEventsText: "Nema doga\u0111aja za prikaz"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return hr;

}());
