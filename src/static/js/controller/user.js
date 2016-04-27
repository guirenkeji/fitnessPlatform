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
dashboard.controller('personnelManagement', ['$scope', '$http', function($scope,$http){

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
}])


dashboard.controller('personnelAdd',['$scope','$http', function($scope,$http){

	$scope.init = function () {
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
                 btn.button('reset');
                 window.location.href = "fitnessmanages#/personnel/management";
             }
        });
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
                 window.location.href = "fitnessmanages#/member/management";
             }
        });
    }
}])

dashboard.controller('memberManagement', ['$scope', '$http', function($scope,$http){
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
		
	
	    $scope.init = function () {
			// App.init();
	    }
}])
