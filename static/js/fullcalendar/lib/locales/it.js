FullCalendar.globalLocales.push(function () {
  'use strict';

  var it = {
<<<<<<< HEAD
    code: 'it',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Prec',
      next: 'Succ',
      today: 'Oggi',
      month: 'Mese',
      week: 'Settimana',
      day: 'Giorno',
      list: 'Agenda',
    },
    weekText: 'Sm',
    allDayText: 'Tutto il giorno',
    moreLinkText: function(n) {
      return '+altri ' + n
    },
    noEventsText: 'Non ci sono eventi da visualizzare',
=======
    code: "it",
    week: {
      dow: 1,
      doy: 4
    },
    buttonText: {
      prev: "Prec",
      next: "Succ",
      today: "Oggi",
      month: "Mese",
      week: "Settimana",
      day: "Giorno",
      list: "Agenda"
    },
    weekText: "Sm",
    allDayText: "Tutto il giorno",
    moreLinkText: function(n) {
      return "+altri " + n;
    },
    noEventsText: "Non ci sono eventi da visualizzare"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return it;

}());
