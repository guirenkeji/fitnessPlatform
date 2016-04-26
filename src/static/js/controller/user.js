// 用户角色
dashboard.controller('userManagement', ['$scope', function($scope){

	$scope.init = function () {
		// App.init();
	};
	$scope.formData = {};
}])


dashboard.controller('userAdd', ['$scope', function($scope){

	$scope.init = function () {
		// App.init();
	}
}])

// 人事管理
dashboard.controller('personnelManagement', ['$scope', function($scope){

	$scope.init = function () {
		// App.init();
	}
}])


dashboard.controller('personnelAdd', ['$scope', function($scope){

	$scope.init = function () {
		// App.init();
	}
}])

// 会员管理
dashboard.controller('memberManagement', ['$scope', function($scope){

	$scope.init = function () {
		// App.init();
		
	}
}])


dashboard.controller('memberAdd',['$scope','$http', function($scope,$http){

	$scope.init = function () {
		// App.init();
		$scope.formdata = {};
	}

	$scope.create = function () {
        
		
        $http({
          method  : 'POST',
          url     : '/fitnessmanages/addMember',
          data    : $scope.formdata, 
          headers : {'Content-Type': 'application/x-www-form-urlencoded'} 
         }).success(function (result) {
        	if (result.created) {
                $scope.AddSuccess = true;
            }
        });
    }
}])