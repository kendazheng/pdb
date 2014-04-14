var publishapp = angular.module('PublishApp', ['ui.bootstrap','PublishCtrls']);
publishapp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
    
publishapp.config(function($httpProvider) {
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
});

angular.element(document).ready(function(){
    angular.bootstrap($('.publish')[0],['PublishApp']);
});
