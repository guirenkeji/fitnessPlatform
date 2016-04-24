dashboard.controller('teamCoursesManagement', ['$scope', function($scope){

	$scope.init = function () {
		// App.init();
	}
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