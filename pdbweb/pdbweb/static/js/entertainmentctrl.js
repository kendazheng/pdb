var entertainmentctrls= angular.module('EntertainmentCtrls', []);

entertainmentctrls.controller('EntertainmentTopCtrl', ['$scope', '$modal', '$http', function($scope, $modal, $http){
    $http.get('/api/entertainment/').success(function(articles){
        console.log(articles);
        $scope.topArticle = articles[0];
        articles.shift(0);        
        $scope.articles = articles;
             
    }).error(function(res){
        
    });
    var data = {
        'author':'root',
        'index':'http://h.hiphotos.baidu.com/image/w%3D2048/sign=24753a258501a18bf0eb154faa170608/42166d224f4a20a4e98280ce92529822720ed01f.jpg',
        'summary':'aaaaaa',
        'title': 'post test',
        'contents':[{
            'title':'asdasdsad',
            'desc':'ddddddd',
            'medias':[{
                'src':'http://h.hiphotos.baidu.com/image/w%3D2048/sign=24753a258501a18bf0eb154faa170608/42166d224f4a20a4e98280ce92529822720ed01f.jpg',
                'media_type':'IMAGE'
            }],
        }],
        'publish_state':true
    };
    /*var data = {
        'album_name':'root',
        'artist':'root',
        'tracks':[{
            'order':2,
            'title':'ssss',
            'duration':2
        }],
    };
    $http.post('/api/entertainment/',data).success(function(res){
        console.log(res);
    }).error(function(res){
        console.log(res)
    });*/
    $http.put('/api/entertainment/2/detail/',data).success(function(res){
        console.log(res);
    }).error(function(res){
        console.log(res)
    });
    
}]);

