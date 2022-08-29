FullCalendar.globalLocales.push(function () {
  'use strict';

  var et = {
<<<<<<< HEAD
    code: 'et',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Eelnev',
      next: 'Järgnev',
      today: 'Täna',
      month: 'Kuu',
      week: 'Nädal',
      day: 'Päev',
      list: 'Päevakord',
    },
    weekText: 'näd',
    allDayText: 'Kogu päev',
    moreLinkText: function(n) {
      return '+ veel ' + n
    },
    noEventsText: 'Kuvamiseks puuduvad sündmused',
=======
    code: "et",
    week: {
      dow: 1,
      doy: 4
    },
    buttonText: {
      prev: "Eelnev",
      next: "J\xE4rgnev",
      today: "T\xE4na",
      month: "Kuu",
      week: "N\xE4dal",
      day: "P\xE4ev",
      list: "P\xE4evakord"
    },
    weekText: "n\xE4d",
    allDayText: "Kogu p\xE4ev",
    moreLinkText: function(n) {
      return "+ veel " + n;
    },
    noEventsText: "Kuvamiseks puuduvad s\xFCndmused"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return et;

}());
