var publishctrls= angular.module('PublishCtrls', ['textAngular']);

publishctrls.controller('PublishCtrl', ['$scope', '$modal', '$http', function($scope, $modal, $http){
    $scope.data = "hello";
}]);

