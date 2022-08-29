FullCalendar.globalLocales.push(function () {
  'use strict';

  var ja = {
<<<<<<< HEAD
    code: 'ja',
    buttonText: {
      prev: '前',
      next: '次',
      today: '今日',
      month: '月',
      week: '週',
      day: '日',
      list: '予定リスト',
    },
    weekText: '週',
    allDayText: '終日',
    moreLinkText: function(n) {
      return '他 ' + n + ' 件'
    },
    noEventsText: '表示する予定はありません',
=======
    code: "ja",
    buttonText: {
      prev: "\u524D",
      next: "\u6B21",
      today: "\u4ECA\u65E5",
      month: "\u6708",
      week: "\u9031",
      day: "\u65E5",
      list: "\u4E88\u5B9A\u30EA\u30B9\u30C8"
    },
    weekText: "\u9031",
    allDayText: "\u7D42\u65E5",
    moreLinkText: function(n) {
      return "\u4ED6 " + n + " \u4EF6";
    },
    noEventsText: "\u8868\u793A\u3059\u308B\u4E88\u5B9A\u306F\u3042\u308A\u307E\u305B\u3093"
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
  };

  return ja;

}());
