dashboard.controller('teamCoursesManagement2', ['$scope', function($scope){

	$scope.init = function () {
		$scope.courselist = {};
		if($("#PageNo").val()){var PageNo = $("#PageNo").val();}else{var PageNo = 1;};
		$http.post('/courses/team/management/add', PageNo,$http).success(function (result) {
        	if (result.data) {
        		$scope.courselist = result.data;
            }
        });
		// App.init();
	}
}])

dashboard.controller('teamCoursesAdd', ['$scope','$http', function($scope,$http){
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