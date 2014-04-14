var basectrls = angular.module('BaseCtrls', []);
basectrls.controller('TopCtrl', ['$scope', '$modal', '$http', function($scope, $modal, $http){
    var urlHighLight = function(){
        var currentNav = $('.main-nav a').filter(function () {
            var pathname = (this.pathname.charAt(0) == "/") ? this.pathname
                  : "/" + this.pathname;
            return window.location.pathname.indexOf(pathname) == 0 && pathname.length <= window.location.pathname.length;
        });
        currentNav.parent().addClass('active');

    };


    $scope.login = function(){
        $modal.open({
            backdropFade: true,
            controller: 'LoginCtrl',
            templateUrl: '/static/template/login.html'
        }).result.then(function(user){});
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

basectrls.controller('LoginCtrl', ['$scope', '$modalInstance', '$http', function($scope, $modalInstance, $http){
    $scope.alerts = [];
    $scope.input= {};
    $scope.cancel = function(){
        $modalInstance.dismiss();
    };

    $scope.ok = function(){
        var username = $scope.input.username;
        var password = $scope.input.password;
        if(username && password){
            var user = {
                'username':username,
                'password':password
            };
            var user = '?username=' + username + '&&password=' + password;
            $http.get('/api/account/' + user).success(function(res){
                if(res['status'] == 0){
                    $modalInstance.dismiss();
                    location.reload() ;
                }
                else{
                    $scope.alerts.push({
                        'msg':res['msg'],
                        'type':'alert-danger'
                    });
                }    
            }).error(function(res){
                $scope.alerts.push({
                    'msg':res['msg'],
                    'type':'alert-danger'
                });
            });        
        }
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

basectrls.controller('RegistryCtrl', ['$scope', '$modalInstance', '$http', function($scope, $modalInstance, $http){
    //$scope.alerts = [{'msg':'aaaaaaaaaaaa','type':'alert-warning'}];
    $scope.alerts = [];
    $scope.input= {};
    $scope.cancel = function(){
        $modalInstance.dismiss();
    };

    $scope.ok = function(){
        var username = $scope.input.username;
        var email = $scope.input.email;
        var password= $scope.input.password;
        var password_again = $scope.input.password_again;
        console.log(username);
        console.log(email);
        console.log(password);
        console.log(password_again);
        if(username && password && password_again && email){
            var user = {
                'username': username,
                'password': password,
                'password_again': password_again,
                'email': email
            }
            $http.post('/api/account/',user).success(function(res){
                $modalInstance.dismiss();
                location.reload();
            }).error(function(res){
            
            });
        }
        else
            $scope.alerts.push({
                'msg':'Username,Password and Email should not be blank!',
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


