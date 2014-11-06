var publishctrls= angular.module('PublishCtrls', ['colorpicker.module', 'wysiwyg.module']);

publishctrls.controller('PublishCtrl', ['$scope', '$modal', '$http', function($scope, $modal, $http){
    $scope.data = {
        text: "hello"
    }
    $scope.textareaHeight = '300px';
}]);

