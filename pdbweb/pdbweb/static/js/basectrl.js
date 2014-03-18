var basectrls = angular.module('BaseCtrls', []);
basectrls.controller('TopCtrl', ['$scope', '$modal', function($scope, $modal){
    $scope.data = 'aaaa';
    var urlHighLight = function(){
        var currentNav = $('.main-nav a').filter(function () {
            var pathname = (this.pathname.charAt(0) == "/") ? this.pathname
                  : "/" + this.pathname;
            return window.location.pathname.indexOf(pathname) == 0 && this.pathname.length >= window.location.pathname.length;
            //return pathname == window.location.pathname;
        });
        currentNav.parent().addClass('active');

    };

    $scope.login = function(){
        $modal.open({
            backdropFade: true,
            controller: 'LoginCtrl',
            templateUrl: '/static/template/login.html'
        }).result.then();
    };

    $scope.registry = function(){
        $modal.open({
            backdropFade: true,
            controller: 'Registry',
            templateUrl: '/static/template/registry.html'
        }).result.then();
    };
    
    urlHighLight();
}]);

basectrls.controller('LoginCtrl', ['$scope', '$modalInstance', function($scope, $modalInstance){
    $scope.alerts = [];
    $scope.cancel = function(){
        $modalInstance.close(undefined);
    };

    $scope.ok = function(){
        $modalInstance.close(undefined);
    };

    $scope.closeAlert = function(index){
        $scope.alerts.splice(index);
    };

    $scope.findPassword = function(){
        window.open('http://www.baidu.com');
    };
}]);

basectrls.controller('Registry', ['$scope', '$modalInstance', function($scope, $modalInstance){
    //$scope.alerts = [{'msg':'aaaaaaaaaaaa','type':'alert-warning'}];
    $scope.alerts = [];
    $scope.cancel = function(){
        $modalInstance.close(undefined);
    };

    $scope.ok = function(){
        $modalInstance.close(undefined);
    };

    $scope.closeAlert = function(index){
        $scope.alerts.splice(index);
    };

    $scope.findPassword = function(){
        window.open('http://www.baidu.com');
    };

}]);


