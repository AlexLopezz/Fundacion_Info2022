FullCalendar.globalLocales.push(function () {
  'use strict';

  var sk = {
<<<<<<< HEAD
    code: 'sk',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Predchádzajúci',
      next: 'Nasledujúci',
      today: 'Dnes',
      month: 'Mesiac',
      week: 'Týždeň',
      day: 'Deň',
      list: 'Rozvrh',
    },
    weekText: 'Ty',
    allDayText: 'Celý deň',
    moreLinkText: function(n) {
      return '+ďalšie: ' + n
    },
    noEventsText: 'Žiadne akcie na zobrazenie',
=======
    code: "sk",
    week: {
      dow: 1,
      doy: 4
    },
    buttonText: {
      prev: "Predch\xE1dzaj\xFAci",
      next: "Nasleduj\xFAci",
      today: "Dnes",
      month: "Mesiac",
      week: "T\xFD\u017Ede\u0148",
      day: "De\u0148",
      list: "Rozvrh"
    },
    weekText: "Ty",
    allDayText: "Cel\xFD de\u0148",
    moreLinkText: function(n) {
      return "+\u010Fal\u0161ie: " + n;
    },
    noEventsText: "\u017Diadne akcie na zobrazenie"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return sk;

}());
