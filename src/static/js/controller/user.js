dashboard.controller('userManagement', ['$scope', function($scope){

	$scope.init = function () {
		// App.init();
	};
	$scope.formData = {};
}])


dashboard.controller('memberAdd', ['$scope', function($scope){

	$scope.init = function () {
		// App.init();
	}
	$scope.create = function () {
        var btn = $("#btnCreate");
        btn.button('loading');
		$scope.Course = {};
        $scope.Course.name = $("#fullname").val();
        $scope.Course.birthday = $("#data-class-time").val();
		$scope.Course.sex=$("#radiorequired").val();
		$scope.Course.phone=$("#data-phone").val();
		$scope.Course.address=$("#data-address").val();
        $scope.Course.wchat=$("#data-wchat").val();
        $scope.Course.comments = $("#message").val();
        $http.post('/fitnessmanages/addMember', $scope.Course).success(function (result) {
        	if (result.created) {
                $scope.AddSuccess = true;
                btn.button('reset');
                window.location.href = "/Project/Task/" + result.ProjectId;
            }
        });
    }
}])