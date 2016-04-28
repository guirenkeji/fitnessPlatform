// 团队课程
dashboard.controller('teamCoursesManagement', ['$scope', '$http', function($scope,$http){
		var self = this;
		$scope.Page = {};
		if($("#PageNo").val()){
			$scope.Page.PageNo = $("#PageNo").val();
		}else{
			$scope.Page.PageNo = 1;
		}
		$http.post('/courses/team/query', $scope.Page, $http).success(function (result) {
	    	if (result.data) {
	    		self.courselist = result.data;
	        }
	    }).error(function (data, status, headers, config) { });
		
		
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

		
		
	
	    $scope.init = function () {
			// App.init();
	    }
}])

dashboard.controller('teamCoursesAdd', ['$scope','$http', function($scope,$http){
    $scope.init = function () {
        FormPlugins.init();
    }

    $scope.create = function () {
        var btn = $("#btnCreate");
        btn.button('loading');

        $scope.Course = {};
        $scope.Course.fullname = $("#fullname").val();
        $scope.Course.dataclasstime = $("#data-class-time").val();
        $scope.Course.message = $("#message").val();

        $http.post('/courses/team/management/add', $scope.Course).success(function (result) {
            if (result.created) {
                $scope.AddSuccess = true;
                btn.button('reset');
                window.location.href = "fitnessmanages#/courses/team/management";
            }
        });
    }
}])

dashboard.controller('teamCoursesUpdate', ['$scope','$http', function($scope,$http){
	$scope.Course = {};
	$scope.Course.Name = "test";
	$scope.update = function () {
        $http.post('/courses/team/management/add', $scope.Course).success(function (result) {
        	if (result.created) {
                alert("Success");
                
            }
        });
    }
}])


// 私教课程
dashboard.controller('privateCoursesManagement', ['$scope', '$http', function($scope,$http){
	var self = this;
	$scope.Page = {};
	if($("#PageNo").val()){
		$scope.Page.PageNo = $("#PageNo").val();
	}else{
		$scope.Page.PageNo = 1;
	}
	$http.post('/courses/private/query', $scope.Page, $http).success(function (result) {
    	if (result.data) {
    		self.courselist = result.data;
        }
    }).error(function (data, status, headers, config) { });

    $scope.init = function () {
		// App.init();
    }
}])


dashboard.controller('privateCoursesAdd', ['$scope','$http', function($scope,$http){
    $scope.create = function () {
        var btn = $("#btnCreate");
        btn.button('loading');

        $scope.Course = {};
        $scope.Course.fullname = $("#fullname").val();
        $scope.Course.dataclasstime = $("#data-class-time").val();
        $scope.Course.message = $("#message").val();

        $http.post('/courses/team/management/add', $scope.Course,$http).then(function (result) {
            if (result.created) {
                $scope.AddSuccess = true;
                btn.button('reset');
                window.location.href = "/Project/Task/" + result.ProjectId;
            }
        });
    }
}])