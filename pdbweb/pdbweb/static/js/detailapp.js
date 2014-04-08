var detailapp = angular.module('DetailApp', ['ui.bootstrap','DetailCtrls']);
detailapp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
    
detailapp.config(function($httpProvider) {
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
});

angular.element(document).ready(function(){
    angular.bootstrap($('.article_detail')[0],['DetailApp']);
});
