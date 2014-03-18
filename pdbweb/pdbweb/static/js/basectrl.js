var basectrls = angular.module('BaseCtrls', []);
basectrls.controller('TopCtrl', ['$scope', '$modal', '$http', function($scope, $modal, $http){
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
        }).result.then(function(user){
            $http.post('/account/login/',{'username':'root','password':'123456'})
                .success(function(res){
                    console.log(res)
                })
                .error(function(res){
                    console.log(res);
                });        
        });
    };

    $scope.registry = function(){
        $modal.open({
            backdropFade: true,
            controller: 'RegistryCtrl',
            templateUrl: '/static/template/registry.html'
        }).result.then();
    };
    
    urlHighLight();
}]);

basectrls.controller('LoginCtrl', ['$scope', '$modalInstance', function($scope, $modalInstance){
    $scope.alerts = [];
    $scope.input= {};
    $scope.cancel = function(){
        $modalInstance.close(undefined);
    };

    $scope.ok = function(){
        if($scope.input.username && $scope.input.password)
            $modalInstance.close({
                username: $scope.input.username,
                password: $scope.input.password
            });
        else
            $scope.alerts.push({
                'msg':'Username and Password should not be blank!',
                'type':'alert-danger'
            });
            
    };

    $scope.closeAlert = function(index){
        $scope.alerts.splice(index);
    };

    $scope.findPassword = function(){
        window.open('http://www.baidu.com');
    };
}]);

basectrls.controller('RegistryCtrl', ['$scope', '$modalInstance', function($scope, $modalInstance){
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


