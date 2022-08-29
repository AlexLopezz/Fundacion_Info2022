FullCalendar.globalLocales.push(function () {
  'use strict';

  var enGb = {
<<<<<<< HEAD
    code: 'en-gb',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonHints: {
      prev: 'Previous $0',
      next: 'Next $0',
      today: 'This $0',
    },
    viewHint: '$0 view',
    navLinkHint: 'Go to $0',
    moreLinkHint(eventCnt) {
      return `Show ${eventCnt} more event${eventCnt === 1 ? '' : 's'}`
    },
=======
    code: "en-gb",
    week: {
      dow: 1,
      doy: 4
    },
    buttonHints: {
      prev: "Previous $0",
      next: "Next $0",
      today: "This $0"
    },
    viewHint: "$0 view",
    navLinkHint: "Go to $0",
    moreLinkHint: function(eventCnt) {
      return "Show ".concat(eventCnt, " more event").concat(eventCnt === 1 ? "" : "s");
    }
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return enGb;

}());
