FullCalendar.globalLocales.push(function () {
  'use strict';

  var cs = {
<<<<<<< HEAD
    code: 'cs',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Dříve',
      next: 'Později',
      today: 'Nyní',
      month: 'Měsíc',
      week: 'Týden',
      day: 'Den',
      list: 'Agenda',
    },
    weekText: 'Týd',
    allDayText: 'Celý den',
    moreLinkText: function(n) {
      return '+další: ' + n
    },
    noEventsText: 'Žádné akce k zobrazení',
=======
    code: "cs",
    week: {
      dow: 1,
      doy: 4
    },
    buttonText: {
      prev: "D\u0159\xEDve",
      next: "Pozd\u011Bji",
      today: "Nyn\xED",
      month: "M\u011Bs\xEDc",
      week: "T\xFDden",
      day: "Den",
      list: "Agenda"
    },
    weekText: "T\xFDd",
    allDayText: "Cel\xFD den",
    moreLinkText: function(n) {
      return "+dal\u0161\xED: " + n;
    },
    noEventsText: "\u017D\xE1dn\xE9 akce k zobrazen\xED"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return cs;

}());
