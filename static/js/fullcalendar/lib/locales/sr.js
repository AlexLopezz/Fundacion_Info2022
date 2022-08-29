FullCalendar.globalLocales.push(function () {
  'use strict';

  var sr = {
<<<<<<< HEAD
    code: 'sr',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 7, // The week that contains Jan 1st is the first week of the year.
    },
    buttonText: {
      prev: 'Prethodna',
      next: 'Sledeći',
      today: 'Danas',
      month: 'Mеsеc',
      week: 'Nеdеlja',
      day: 'Dan',
      list: 'Planеr',
    },
    weekText: 'Sed',
    allDayText: 'Cеo dan',
    moreLinkText: function(n) {
      return '+ još ' + n
    },
    noEventsText: 'Nеma događaja za prikaz',
=======
    code: "sr",
    week: {
      dow: 1,
      doy: 7
    },
    buttonText: {
      prev: "Prethodna",
      next: "Sledec\u0301i",
      today: "Danas",
      month: "M\u0435s\u0435c",
      week: "N\u0435d\u0435lja",
      day: "Dan",
      list: "Plan\u0435r"
    },
    weekText: "Sed",
    allDayText: "C\u0435o dan",
    moreLinkText: function(n) {
      return "+ jo\u0161 " + n;
    },
    noEventsText: "N\u0435ma doga\u0111aja za prikaz"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return sr;

}());
