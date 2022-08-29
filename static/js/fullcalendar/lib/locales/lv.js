FullCalendar.globalLocales.push(function () {
  'use strict';

  var lv = {
<<<<<<< HEAD
    code: 'lv',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Iepr.',
      next: 'Nāk.',
      today: 'Šodien',
      month: 'Mēnesis',
      week: 'Nedēļa',
      day: 'Diena',
      list: 'Dienas kārtība',
    },
    weekText: 'Ned.',
    allDayText: 'Visu dienu',
    moreLinkText: function(n) {
      return '+vēl ' + n
    },
    noEventsText: 'Nav notikumu',
=======
    code: "lv",
    week: {
      dow: 1,
      doy: 4
    },
    buttonText: {
      prev: "Iepr.",
      next: "N\u0101k.",
      today: "\u0160odien",
      month: "M\u0113nesis",
      week: "Ned\u0113\u013Ca",
      day: "Diena",
      list: "Dienas k\u0101rt\u012Bba"
    },
    weekText: "Ned.",
    allDayText: "Visu dienu",
    moreLinkText: function(n) {
      return "+v\u0113l " + n;
    },
    noEventsText: "Nav notikumu"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return lv;

}());
