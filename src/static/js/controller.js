dashboard.controller('sidebar', ['$scope', '$rootScope', function($scope, $rootScope){

	$scope.init = function () {
		// App.init();
		console.log($rootScope.path);
	}
}])
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
dashboard.controller('teamCoursesAdd', ['$scope','$http', function($scope,$http){
    $scope.create = function () {
        var btn = $("#btnCreate");
        btn.button('loading');
        $http.post('/courses/team/management/add', $scope.Course).success(function (result) {
        	if (result.created) {
                $scope.AddSuccess = true;
                btn.button('reset');
                window.location.href = "/Project/Task/" + result.ProjectId;
            }
        });
    }
}])