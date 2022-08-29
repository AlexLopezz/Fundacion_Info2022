FullCalendar.globalLocales.push(function () {
  'use strict';

  var bn = {
<<<<<<< HEAD
    code: 'bn',
    week: {
      dow: 0, // Sunday is the first day of the week.
      doy: 6, // The week that contains Jan 1st is the first week of the year.
    },
    buttonText: {
      prev: 'পেছনে',
      next: 'সামনে',
      today: 'আজ',
      month: 'মাস',
      week: 'সপ্তাহ',
      day: 'দিন',
      list: 'তালিকা',
    },
    weekText: 'সপ্তাহ',
    allDayText: 'সারাদিন',
    moreLinkText: function(n) {
      return '+অন্যান্য ' + n
    },
    noEventsText: 'কোনো ইভেন্ট নেই',
=======
    code: "bn",
    week: {
      dow: 0,
      doy: 6
    },
    buttonText: {
      prev: "\u09AA\u09C7\u099B\u09A8\u09C7",
      next: "\u09B8\u09BE\u09AE\u09A8\u09C7",
      today: "\u0986\u099C",
      month: "\u09AE\u09BE\u09B8",
      week: "\u09B8\u09AA\u09CD\u09A4\u09BE\u09B9",
      day: "\u09A6\u09BF\u09A8",
      list: "\u09A4\u09BE\u09B2\u09BF\u0995\u09BE"
    },
    weekText: "\u09B8\u09AA\u09CD\u09A4\u09BE\u09B9",
    allDayText: "\u09B8\u09BE\u09B0\u09BE\u09A6\u09BF\u09A8",
    moreLinkText: function(n) {
      return "+\u0985\u09A8\u09CD\u09AF\u09BE\u09A8\u09CD\u09AF " + n;
    },
    noEventsText: "\u0995\u09CB\u09A8\u09CB \u0987\u09AD\u09C7\u09A8\u09CD\u099F \u09A8\u09C7\u0987"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return bn;

}());
