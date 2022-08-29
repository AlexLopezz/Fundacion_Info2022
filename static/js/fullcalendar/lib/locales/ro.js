FullCalendar.globalLocales.push(function () {
  'use strict';

  var ro = {
<<<<<<< HEAD
    code: 'ro',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 7, // The week that contains Jan 1st is the first week of the year.
    },
    buttonText: {
      prev: 'precedentă',
      next: 'următoare',
      today: 'Azi',
      month: 'Lună',
      week: 'Săptămână',
      day: 'Zi',
      list: 'Agendă',
    },
    weekText: 'Săpt',
    allDayText: 'Toată ziua',
    moreLinkText: function(n) {
      return '+alte ' + n
    },
    noEventsText: 'Nu există evenimente de afișat',
=======
    code: "ro",
    week: {
      dow: 1,
      doy: 7
    },
    buttonText: {
      prev: "precedent\u0103",
      next: "urm\u0103toare",
      today: "Azi",
      month: "Lun\u0103",
      week: "S\u0103pt\u0103m\xE2n\u0103",
      day: "Zi",
      list: "Agend\u0103"
    },
    weekText: "S\u0103pt",
    allDayText: "Toat\u0103 ziua",
    moreLinkText: function(n) {
      return "+alte " + n;
    },
    noEventsText: "Nu exist\u0103 evenimente de afi\u0219at"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return ro;

}());
