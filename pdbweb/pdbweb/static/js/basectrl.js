var basectrls = angular.module('BaseCtrls', []);
basectrls.controller('TopCtrl', ['$scope', '$modal', function($scope, $modal){
    $scope.data = 'aaaa';
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


