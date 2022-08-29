FullCalendar.globalLocales.push(function () {
  'use strict';

  var sv = {
<<<<<<< HEAD
    code: 'sv',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Förra',
      next: 'Nästa',
      today: 'Idag',
      month: 'Månad',
      week: 'Vecka',
      day: 'Dag',
      list: 'Program',
    },
    buttonHints: {
      prev(buttonText) {
        return `Föregående ${buttonText.toLocaleLowerCase()}`
      },
      next(buttonText) {
        return `Nästa ${buttonText.toLocaleLowerCase()}`
      },
      today(buttonText) {
        return (buttonText === 'Program' ? 'Detta' : 'Denna') + ' ' + buttonText.toLocaleLowerCase()
      },
    },
    viewHint: '$0 vy',
    navLinkHint: 'Gå till $0',
    moreLinkHint(eventCnt) {
      return `Visa ytterligare ${eventCnt} händelse${eventCnt === 1 ? '' : 'r'}`
    },
    weekText: 'v.',
    weekTextLong: 'Vecka',
    allDayText: 'Heldag',
    moreLinkText: 'till',
    noEventsText: 'Inga händelser att visa',
    closeHint: 'Stäng',
    timeHint: 'Klockan',
    eventHint: 'Händelse',
=======
    code: "sv",
    week: {
      dow: 1,
      doy: 4
    },
    buttonText: {
      prev: "F\xF6rra",
      next: "N\xE4sta",
      today: "Idag",
      month: "M\xE5nad",
      week: "Vecka",
      day: "Dag",
      list: "Program"
    },
    buttonHints: {
      prev: function(buttonText) {
        return "F\xF6reg\xE5ende ".concat(buttonText.toLocaleLowerCase());
      },
      next: function(buttonText) {
        return "N\xE4sta ".concat(buttonText.toLocaleLowerCase());
      },
      today: function(buttonText) {
        return (buttonText === "Program" ? "Detta" : "Denna") + " " + buttonText.toLocaleLowerCase();
      }
    },
    viewHint: "$0 vy",
    navLinkHint: "G\xE5 till $0",
    moreLinkHint: function(eventCnt) {
      return "Visa ytterligare ".concat(eventCnt, " h\xE4ndelse").concat(eventCnt === 1 ? "" : "r");
    },
    weekText: "v.",
    weekTextLong: "Vecka",
    allDayText: "Heldag",
    moreLinkText: "till",
    noEventsText: "Inga h\xE4ndelser att visa",
    closeHint: "St\xE4ng",
    timeHint: "Klockan",
    eventHint: "H\xE4ndelse"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return sv;

}());
