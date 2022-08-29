FullCalendar.globalLocales.push(function () {
  'use strict';

  var az = {
<<<<<<< HEAD
    code: 'az',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Əvvəl',
      next: 'Sonra',
      today: 'Bu Gün',
      month: 'Ay',
      week: 'Həftə',
      day: 'Gün',
      list: 'Gündəm',
    },
    weekText: 'Həftə',
    allDayText: 'Bütün Gün',
    moreLinkText: function(n) {
      return '+ daha çox ' + n
    },
    noEventsText: 'Göstərmək üçün hadisə yoxdur',
=======
    code: "az",
    week: {
      dow: 1,
      doy: 4
    },
    buttonText: {
      prev: "\u018Fvv\u0259l",
      next: "Sonra",
      today: "Bu G\xFCn",
      month: "Ay",
      week: "H\u0259ft\u0259",
      day: "G\xFCn",
      list: "G\xFCnd\u0259m"
    },
    weekText: "H\u0259ft\u0259",
    allDayText: "B\xFCt\xFCn G\xFCn",
    moreLinkText: function(n) {
      return "+ daha \xE7ox " + n;
    },
    noEventsText: "G\xF6st\u0259rm\u0259k \xFC\xE7\xFCn hadis\u0259 yoxdur"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return az;

}());
