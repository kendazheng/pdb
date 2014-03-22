var entertainmentapp = angular.module('EntertainmentApp', ['ui.bootstrap','EntertainmentCtrls']);
entertainmentapp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
    
entertainmentapp.config(function($httpProvider) {
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
});

angular.element(document).ready(function(){
    angular.bootstrap($('.entertainment')[0],['EntertainmentApp']);
});
