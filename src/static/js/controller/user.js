
// 用户角色
dashboard.controller('userManagement', ['$scope','$http', function($scope,$http){
//	$scpoe.query();
	$scope.Query = { PageNo: 1, role: ''};
	$scope.init = function () {
		// App.init();
	};
	$scope.formData = {};
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
        $http.post('/role/query',$scope.Query).success(function (result) {
            btn.button('reset');
            $scope.RoleList = result.data;

        });
    }    

}])

dashboard.controller('userAdd', ['$scope','$http', function($scope,$http){

    $scope.create = function () {
        $http.post('/role/add', $scope.role).success(function (result) {
        	if (result.created) {
                alert("Success");
                window.location.href = 'fitnessmanages#/user/management'
            }
        });
    }
	
}])




dashboard.controller('userModify', ['$scope', function($scope){

	$scope.init = function () {
		FormPlugins.init();
	}
}])

// 人事管理
dashboard.controller('personnelManagement', ['$scope', '$http', '$route',function($scope,$http,$route){

	$scope.init = function () {
		// App.init();
	}
	
	var self = this;
	$scope.Page = {};
	if($("#PageNo").val()){
		$scope.Page.PageNo = $("#PageNo").val();
	}else{
		$scope.Page.PageNo = 1;
	}
	$scope.Page.searchKey='';
	$http.post('/fitnessmanages/searchEmployee', $scope.Page, $http).success(function (result) {
    	if (result.data) {
    		$scope.employeelist = result.data;
    		
        }
    }).error(function (data, status, headers, config) { });
	
	$scope.Delete = function (employeeID) {
        var btn = $("#btnDelete");
        btn.button('loading');
        $http.post('/fitnessmanages/deleteEmployee', { id: employeeID }).success(function (result) {
            if (result.deleted) {
                $scope.DeleteSuccess = true;
                btn.button('reset');
//                window.location.href = 'fitnessmanages#/memeber/management';
                $route.reload();
            }
        });
    }
	
}])


dashboard.controller('personalAdd',['$scope','$http', function($scope,$http){

	$scope.init = function () {
//		FormPlugins.init();
	}
	
	$scope.create = function () {
        
		 var btn = $("#btnCreate");
	     btn.button('loading');
	        
       $http({
         method  : 'POST',
         url     : '/fitnessmanages/addEmployee',
         data    : $scope.formdata, 
         headers : {'Content-Type': 'application/json'} 
        }).success(function (result) {
       	 if (result.created) {
                $scope.AddSuccess = true;
                btn.button('reset');
                window.location.href = "fitnessmanages#/personnel/management";
            }
       });
   }
}])

dashboard.controller('personalModify', ['$scope', function($scope){

	$scope.init = function () {
		FormPlugins.init();
		// App.init();
		$scope.formdata = {};
	}

	$scope.create = function () {
        
		 var btn = $("#btnCreate");
	     btn.button('loading');
	        
        $http({
          method  : 'POST',
          url     : '/fitnessmanages/addEmployee',
          data    : $scope.formdata, 
          headers : {'Content-Type': 'application/json'} 
         }).success(function (result) {
        	 if (result.created) {
                 $scope.AddSuccess = true;
                 $route.reload();
                 window.location.href = "fitnessmanages#/personnel/management";
             }
        });
    }
}])

//会员管理
dashboard.controller('memberAdd',['$scope','$http', function($scope,$http){

	$scope.init = function () {
//		FormPlugins.init();
		$scope.formdata = {};
	}

	$scope.create = function () {
        
		 var btn = $("#btnCreate");
	     btn.button('loading');
	        
        $http({
          method  : 'POST',
          url     : '/fitnessmanages/addMember',
          data    : $scope.formdata, 
          headers : {'Content-Type': 'application/json'} 
         }).success(function (result) {
        	 if (result.created) {
                 $scope.AddSuccess = true;
                 btn.button('reset');
                 $route.reload();
                 window.location.href = "fitnessmanages#/member/management";
             }
        });
    }
}])

dashboard.controller('memberModify', ['$scope', function($scope){

	$scope.init = function () {
		FormPlugins.init();
	}
}])

dashboard.controller('memberManagement', ['$scope', '$http','$route', function($scope,$http,$route){
		var self = this;
		$scope.Page = {};
		if($("#PageNo").val()){
			$scope.Page.PageNo = $("#PageNo").val();
		}else{
			$scope.Page.PageNo = 1;
		}
		$scope.Page.searchKey='';
		$http.post('/fitnessmanages/searchMember', $scope.Page, $http).success(function (result) {
	    	if (result.data) {
	    		$scope.memberlist = result.data;
	    		
	        }
	    }).error(function (data, status, headers, config) { });
		
		$scope.Delete = function (memberID) {
	        var btn = $("#btnDelete");
	        btn.button('loading');
	        $http.post('/fitnessmanages/deleteMember', { id: memberID }).success(function (result) {
	            if (result.deleted) {
	                $scope.DeleteSuccess = true;
	                btn.button('reset');
//	                window.location.href = 'fitnessmanages#/memeber/management';
	                $route.reload();
	            }
	        });
	    }
		
	
	    $scope.init = function () {
			// App.init();
	    }
}])
