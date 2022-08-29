FullCalendar.globalLocales.push(function () {
  'use strict';

  var sq = {
<<<<<<< HEAD
    code: 'sq',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'mbrapa',
      next: 'Përpara',
      today: 'sot',
      month: 'Muaj',
      week: 'Javë',
      day: 'Ditë',
      list: 'Listë',
    },
    weekText: 'Ja',
    allDayText: 'Gjithë ditën',
    moreLinkText: function(n) {
      return '+më tepër ' + n
    },
    noEventsText: 'Nuk ka evente për të shfaqur',
=======
    code: "sq",
    week: {
      dow: 1,
      doy: 4
    },
    buttonText: {
      prev: "mbrapa",
      next: "P\xEBrpara",
      today: "sot",
      month: "Muaj",
      week: "Jav\xEB",
      day: "Dit\xEB",
      list: "List\xEB"
    },
    weekText: "Ja",
    allDayText: "Gjith\xEB dit\xEBn",
    moreLinkText: function(n) {
      return "+m\xEB tep\xEBr " + n;
    },
    noEventsText: "Nuk ka evente p\xEBr t\xEB shfaqur"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return sq;

}());
