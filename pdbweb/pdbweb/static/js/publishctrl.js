var publishctrls= angular.module('PublishCtrls', []);

publishctrls.controller('PublishCtrl', ['$scope', '$modal', '$http', function($scope, $modal, $http){
    ('#edit').wysiwyg();    
}]);

