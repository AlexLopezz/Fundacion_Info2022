FullCalendar.globalLocales.push(function () {
  'use strict';

  var ptBr = {
<<<<<<< HEAD
    code: 'pt-br',
    buttonText: {
      prev: 'Anterior',
      next: 'Próximo',
      today: 'Hoje',
      month: 'Mês',
      week: 'Semana',
      day: 'Dia',
      list: 'Lista',
    },
    weekText: 'Sm',
    allDayText: 'dia inteiro',
    moreLinkText: function(n) {
      return 'mais +' + n
    },
    noEventsText: 'Não há eventos para mostrar',
=======
    code: "pt-br",
    buttonText: {
      prev: "Anterior",
      next: "Pr\xF3ximo",
      today: "Hoje",
      month: "M\xEAs",
      week: "Semana",
      day: "Dia",
      list: "Lista"
    },
    weekText: "Sm",
    allDayText: "dia inteiro",
    moreLinkText: function(n) {
      return "mais +" + n;
    },
    noEventsText: "N\xE3o h\xE1 eventos para mostrar"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return ptBr;

}());
