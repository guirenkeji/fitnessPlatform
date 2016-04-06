dashboard.controller('sidebar', ['$scope', function($scope){

	$scope.init = function () {
		// App.init();
	}
}])


//function LoginCtrl($scope, $http) {
dashboard.controller('LoginCtrl', ['$scope','$http', function($scope,$http){
	    $scope.isMatch = true;
	    $scope.isDisabled = false;
	    $scope.login = function () 
	    {
	        $scope.isMatch = true;
	        $scope.isDisabled = false;
	        var btn = $("#btnLogin");
	        btn.button('loading');
	        $http.post('/Login', $scope.User).success(function (result) 
	        {
	            btn.button('reset');
	            if (result.isMatch != null) 
	            {
	                $scope.isMatch = result.isMatch;
	            }
	            if (result.isDisabled != null) 
	            {
	                $scope.isDisabled = result.isDisabled;
	            }
	            if (result.isMatch != null && result.isMatch) 
	            {
	                window.location.href = '/fitnessmanages';
	            }
	        });
	    };
	}])

//dashboard.controller('isoMake', ['$scope', function($scope){
//
//	$scope.init = function () {
//		// App.init();
//	}
//}])
//
//dashboard.controller('appCreate', ['$scope', function($scope){
//
//	$scope.init = function () {
//		// App.init();
//	}
//}])
//
//dashboard.controller('appStatus', ['$scope', function($scope){
//
//	$scope.init = function () {
//		// App.init();
//	}
//}])