var detailctrls= angular.module('DetailCtrls', []);

detailctrls.controller('DetailCtrl', ['$scope', '$modal', '$http', function($scope, $modal, $http){
    $scope.articles = [];
    $scope.next = '';
    var article_tag = Article_Tag;
    var article_id = Article_Id;
    $http.get('/api/' + article_tag + '/detail/' + article_id + '/').success(function(articles){
        console.log(articles);
        $scope.load = "Load More";
        $scope.topArticle = articles['results'][0];
        articles['results'].shift(0);        
        $scope.articles = articles['results'];
        if(articles['next'])
            $scope.next = articles['next'];
             
    }).error(function(res){
        
    });
    var data = {
        'author':'root',
        'index':'http://h.hiphotos.baidu.com/image/w%3D2048/sign=24753a258501a18bf0eb154faa170608/42166d224f4a20a4e98280ce92529822720ed01f.jpg',
        'summary':'aaaaaa',
        'title': 'post test id',
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
    $http.get('/api/entertainment/2/detail/').success(function(res){
        console.log(res);
    }).error(function(res){
        console.log(res)
    });
    
    $scope.more = function(){
        if($scope.next){
            $http.get($scope.next).success(function(res){
                $scope.articles = $scope.articles.concat(res['results'])
                $scope.next = res['next'];
                if(!$scope.next)
                    $scope.load = "The End";
            }).error(function(res){
                console.log(res) 
            });
        } 
    }
    
}]);

