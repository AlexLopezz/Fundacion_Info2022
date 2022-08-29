FullCalendar.globalLocales.push(function () {
  'use strict';

  function affix(buttonText) {
<<<<<<< HEAD
    return (buttonText === 'Tag' || buttonText === 'Monat') ? 'r' :
      buttonText === 'Jahr' ? 's' : ''
  }

  var de = {
    code: 'de',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Zurück',
      next: 'Vor',
      today: 'Heute',
      year: 'Jahr',
      month: 'Monat',
      week: 'Woche',
      day: 'Tag',
      list: 'Terminübersicht',
    },
    weekText: 'KW',
    weekTextLong: 'Woche',
    allDayText: 'Ganztägig',
    moreLinkText: function(n) {
      return '+ weitere ' + n
    },
    noEventsText: 'Keine Ereignisse anzuzeigen',
    buttonHints: {
      prev(buttonText) {
        return `Vorherige${affix(buttonText)} ${buttonText}`
      },
      next(buttonText) {
        return `Nächste${affix(buttonText)} ${buttonText}`
      },
      today(buttonText) {
        // → Heute, Diese Woche, Dieser Monat, Dieses Jahr
        if (buttonText === 'Tag') {
          return 'Heute'
        }
        return `Diese${affix(buttonText)} ${buttonText}`
      },
    },
    viewHint(buttonText) {
      // → Tagesansicht, Wochenansicht, Monatsansicht, Jahresansicht
      const glue = buttonText === 'Woche' ? 'n' : buttonText === 'Monat' ? 's' : 'es';
      return buttonText + glue + 'ansicht'
    },
    navLinkHint: 'Gehe zu $0',
    moreLinkHint(eventCnt) {
      return 'Zeige ' + (eventCnt === 1 ?
        'ein weiteres Ereignis' :
        eventCnt + ' weitere Ereignisse')
    },
    closeHint: 'Schließen',
    timeHint: 'Uhrzeit',
    eventHint: 'Ereignis',
=======
    return buttonText === "Tag" || buttonText === "Monat" ? "r" : buttonText === "Jahr" ? "s" : "";
  }
  var de = {
    code: "de",
    week: {
      dow: 1,
      doy: 4
    },
    buttonText: {
      prev: "Zur\xFCck",
      next: "Vor",
      today: "Heute",
      year: "Jahr",
      month: "Monat",
      week: "Woche",
      day: "Tag",
      list: "Termin\xFCbersicht"
    },
    weekText: "KW",
    weekTextLong: "Woche",
    allDayText: "Ganzt\xE4gig",
    moreLinkText: function(n) {
      return "+ weitere " + n;
    },
    noEventsText: "Keine Ereignisse anzuzeigen",
    buttonHints: {
      prev: function(buttonText) {
        return "Vorherige".concat(affix(buttonText), " ").concat(buttonText);
      },
      next: function(buttonText) {
        return "N\xE4chste".concat(affix(buttonText), " ").concat(buttonText);
      },
      today: function(buttonText) {
        if (buttonText === "Tag") {
          return "Heute";
        }
        return "Diese".concat(affix(buttonText), " ").concat(buttonText);
      }
    },
    viewHint: function(buttonText) {
      var glue = buttonText === "Woche" ? "n" : buttonText === "Monat" ? "s" : "es";
      return buttonText + glue + "ansicht";
    },
    navLinkHint: "Gehe zu $0",
    moreLinkHint: function(eventCnt) {
      return "Zeige " + (eventCnt === 1 ? "ein weiteres Ereignis" : eventCnt + " weitere Ereignisse");
    },
    closeHint: "Schlie\xDFen",
    timeHint: "Uhrzeit",
    eventHint: "Ereignis"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return de;

}());
