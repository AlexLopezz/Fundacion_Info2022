FullCalendar.globalLocales.push(function () {
  'use strict';

  var es = {
<<<<<<< HEAD
    code: 'es',
    week: {
      dow: 1, // Monday is the first day of the week.
      doy: 4, // The week that contains Jan 4th is the first week of the year.
    },
    buttonText: {
      prev: 'Ant',
      next: 'Sig',
      today: 'Hoy',
      month: 'Mes',
      week: 'Semana',
      day: 'Día',
      list: 'Agenda',
    },
    buttonHints: {
      prev: '$0 antes',
      next: '$0 siguiente',
      today(buttonText) {
        return (buttonText === 'Día') ? 'Hoy' :
          ((buttonText === 'Semana') ? 'Esta' : 'Este') + ' ' + buttonText.toLocaleLowerCase()
      },
    },
    viewHint(buttonText) {
      return 'Vista ' + (buttonText === 'Semana' ? 'de la' : 'del') + ' ' + buttonText.toLocaleLowerCase()
    },
    weekText: 'Sm',
    weekTextLong: 'Semana',
    allDayText: 'Todo el día',
    moreLinkText: 'más',
    moreLinkHint(eventCnt) {
      return `Mostrar ${eventCnt} eventos más`
    },
    noEventsText: 'No hay eventos para mostrar',
    navLinkHint: 'Ir al $0',
    closeHint: 'Cerrar',
    timeHint: 'La hora',
    eventHint: 'Evento',
=======
    code: "es",
    week: {
      dow: 1,
      doy: 4
    },
    buttonText: {
      prev: "Ant",
      next: "Sig",
      today: "Hoy",
      month: "Mes",
      week: "Semana",
      day: "D\xEDa",
      list: "Agenda"
    },
    buttonHints: {
      prev: "$0 antes",
      next: "$0 siguiente",
      today: function(buttonText) {
        return buttonText === "D\xEDa" ? "Hoy" : (buttonText === "Semana" ? "Esta" : "Este") + " " + buttonText.toLocaleLowerCase();
      }
    },
    viewHint: function(buttonText) {
      return "Vista " + (buttonText === "Semana" ? "de la" : "del") + " " + buttonText.toLocaleLowerCase();
    },
    weekText: "Sm",
    weekTextLong: "Semana",
    allDayText: "Todo el d\xEDa",
    moreLinkText: "m\xE1s",
    moreLinkHint: function(eventCnt) {
      return "Mostrar ".concat(eventCnt, " eventos m\xE1s");
    },
    noEventsText: "No hay eventos para mostrar",
    navLinkHint: "Ir al $0",
    closeHint: "Cerrar",
    timeHint: "La hora",
    eventHint: "Evento"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return es;

}());
