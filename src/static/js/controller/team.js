dashboard.controller('teamCoursesManagement', ['$scope', function($scope){

	$scope.init = function () {
		// App.init();
	}
}])

dashboard.controller('teamCoursesAdd', ['$scope','$http', function($scope,$http){
    $scope.init = function () {
        FormPlugins.init();
    }
    
    $scope.create = function () {
        
        $scope.Course = {};
        $scope.Course.fullname = $("#fullname").val();
        $scope.Course.dataclasstime = $("#data-class-time").val();
        $scope.Course.message = $("#message").val();
        $http.post('/courses/team/management/add', $scope.Course,$http).success(function (result) {
        	if (result.created) {
                alert("Success");
                
            }
        });
    }
}])