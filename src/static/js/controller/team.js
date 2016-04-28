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
	
	$scope.Delete = function () {
        var btn = $("#btnDelete");
        btn.button('loading');
        $http.post('/Delete', { CourseId: $scope.Course.id }).success(function (result) {
            if (result.deleted) {
                $scope.DeleteSuccess = true;
                btn.button('reset');
                window.location.href = 'fitnessmanages#/courses/team/management';
            }
        });
    }
    $scope.update = function () {
        var btn = $("#btnUpdate");
        btn.button('loading');
        $http.post('/Update', $scope.Course).success(function (result) {
            if (result.updated) {
                $scope.UpdateSuccess = true;
                btn.button('reset');
                window.location.href = 'fitnessmanages#/courses/team/management';
            }
        });
    }
    $scope.query = function () {
        var btn = $("#btnQuery");
        btn.button('loading');
        $http.post('/query', $scope.Query).success(function (result) {
            btn.button('reset');
            $scope.Curse = result.data;
            $scope.Query.RowCount = result.row_count;
            $scope.Query.PageCount = result.page_count;
            $scope.Query.PageNo = result.page_no;
        });
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