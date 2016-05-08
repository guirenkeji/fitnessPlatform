//通用方法
dashboard.filter('getById', function() {
  return function(input, id) {
    var i=0, len=input.length;
    for (; i<len; i++) {
      if (+input[i].id == +id) {
        return input[i];
      }
    }
    return null;
  }
});
// 用户角色
dashboard.controller('userManagement', ['$scope','$http', '$route',function($scope,$http,$route){
//	$scpoe.query();
	$scope.Query = { PageNo: 1, role: ''};
	$scope.init = function () {
		// App.init();
	};
	$scope.formData = {};
	$scope.Delete = function (roleID) {
        var btn = $("#btnDelete");
        btn.button('loading');
        $http.post('/role/delete', { roleID: roleID }).success(function (result) {
            if (result.deleted) {
                $scope.DeleteSuccess = true;
                $route.reload();
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
	$scope.init = function () {
		// FormPlugins.init();
	}
	
    $scope.create = function () {
        $http.post('/role/add', $scope.formData).success(function (result) {
        	if (result.created) {
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
dashboard.service('selectEmployeeID', function() {
    var stringValue = '';
    var objectValue = {
        data: ''
    };
    
    return {
        getString: function() {
            return stringValue;
        },
        setString: function(value) {
            stringValue = value;
        },
        getObject: function() {
            return objectValue;
        }
    }
});
dashboard.controller('personnelManagement', ['$scope', '$http', '$route', 'selectEmployeeID',function($scope,$http,$route,selectEmployeeID){

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
	$http.post('/fitnessmanages/searchEmployee', $scope.Page).success(function (result) {
    	if (result.got) {
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
    };
	
	$scope.Modify = function (employeeID) {
		selectEmployeeID.setString(employeeID)
        window.location.href = 'fitnessmanages#/personnel/management/modify';
    };
    
    $scope.search= function (key){
    	$scope.find={};
    	$scope.find.PageNo=0
    	$scope.find.searchKey=key;
    	$http.post('/fitnessmanages/searchEmployee', $scope.find).success(function (result) {
        	if (result.got) {
        		$scope.employeelist = result.data;
        		
            }
        });
    }
    
    
	
}])


dashboard.controller('personnelAdd',['$scope','$http', function($scope,$http){

	$scope.init = function () {
		FormPlugins.init();
	}
	
	$scope.rolelist=[];
	$http.post('/role/query',{"searchName":""}).success(function (result) {
		if (result.got) {
            $scope.rolelist=result.data;
        }
		
	 });
	
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

dashboard.controller('personnelModify',['$scope','$http','$filter','selectEmployeeID', function($scope,$http,$filter,selectEmployeeID){

	$scope.init = function () {
//		FormPlugins.init();
		// App.init();
		
	}
	
	$scope.rolelist=[];
	$http.post('/role/query',{"searchName":""}).success(function (result) {
		if (result.got) {
            $scope.rolelist=result.data;
        }
		
	 });
	
	$scope.formdata = {};
	$http.post('/fitnessmanages/getEmployee', { id: selectEmployeeID.getString() }).success(function (result) {
        if (result.got) {
//            window.location.href = 'fitnessmanages#/memeber/management';
//            $route.reload();
            $scope.formdata=result.data
            $scope.formdata['id']=selectEmployeeID.getString()
            $scope.formdata['role'] = $filter('getById')($scope.rolelist, $scope.formdata['role']);
        }
    });
	
	

	$scope.modify = function () {
        
		 var btn = $("#btnCreate");
	     btn.button('loading');
         $http.post('/fitnessmanages/modifyEmployee', $scope.formdata).success(function (result) {
        	 if (result.updated) {
                 $scope.AddSuccess = true;
                 window.location.href = "fitnessmanages#/personnel/management";
             }
        });
    }
	
	$scope.update = function () {
        
		var btn = $("#btnCreate");
	     btn.button('loading');
	        
      $http({
        method  : 'POST',
        url     : '/fitnessmanages/modifyEmployee',
        data    : $scope.formdata, 
        headers : {'Content-Type': 'application/json'} 
       }).success(function (result) {
      	 if (result.updated) {
               btn.button('reset');
               window.location.href = "fitnessmanages#/personnel/management";
           }
      });
  }
}])

//会员管理
dashboard.service('selectMemberID', function() {
    var stringValue = '';
    var objectValue = {
        data: ''
    };
    
    return {
        getString: function() {
            return stringValue;
        },
        setString: function(value) {
            stringValue = value;
        },
        getObject: function() {
            return objectValue;
        }
    }
});
dashboard.controller('memberAdd',['$scope','$http', function($scope,$http){

	$scope.init = function () {
//		FormPlugins.init();
		$scope.formdata = {};
	}
	
	$scope.coachlist=[];
	$scope.Page = {};
	if($("#PageNo").val()){
		$scope.Page.PageNo = $("#PageNo").val();
	}else{
		$scope.Page.PageNo = 1;
	}
	$scope.Page.searchKey='教练';
	$http.post('/fitnessmanages/searchEmployeeByRole',$scope.Page).success(function (result) {
		if (result.got) {
            $scope.coachlist=result.data;
        }
		
	 });
	
	$scope.rolelist=[];
	$http.post('/role/query',{"searchName":"会员"}).success(function (result) {
		if (result.got) {
            $scope.rolelist=result.data;
        }
		
	 });

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
//                 $route.reload();
                 window.location.href = "fitnessmanages#/member/management";
             }
        });
    }
	
	$scope.changeMemebrId=function(){
		$http.post('/fitnessmanages/getMember',{'id':$scope.formdata.memberid}).success(function (result) {
			if (result.got) {
	            if (result.data){
	            	var btn = $("#iderror");
	       	        btn.removeClass('hidden');
	            }
	        }
			
		 }).error(function(){
			 var btn = $("#iderror");
	        btn.addClass('hidden');
	        });
	}
}])

dashboard.controller('memberModify',['$scope','$http','$filter','selectMemberID', function($scope,$http,$filter,selectMemberID){

	$scope.init = function () {
//		FormPlugins.init();
		// App.init();
		
	}
	
	$scope.changeMemebrId=function(){
		$http.post('/fitnessmanages/getMember',{'id':$scope.formdata.memberid}).success(function (result) {
			if (result.got) {
	            if (result.data){
	            	var btn = $("#iderror");
	       	        btn.removeClass('hidden');
	            }
	        }
			
		 }).error(function(){
			 var btn = $("#iderror");
	        btn.addClass('hidden');
	        });
	}
	
	$scope.coachlist=[];
	$scope.Page = {};
	if($("#PageNo").val()){
		$scope.Page.PageNo = $("#PageNo").val();
	}else{
		$scope.Page.PageNo = 1;
	}
	$scope.Page.searchKey='教练';
	$http.post('/fitnessmanages/searchEmployeeByRole',$scope.Page).success(function (result) {
		if (result.got) {
            $scope.coachlist=result.data;
        }
		
	 });
	
	$scope.formdata = {};
	$http.post('/fitnessmanages/getMember', { id: selectMemberID.getString() }).success(function (result) {
        if (result.got) {
//            window.location.href = 'fitnessmanages#/memeber/management';
//            $route.reload();
            $scope.formdata=result.data
            $scope.formdata['id']=selectMemberID.getString()
            $scope.formdata['memberid']=$scope.formdata['id']
            $scope.formdata['coach'] = $filter('getById')($scope.coachlist, $scope.formdata['coach_id']);
        }
    });
	
	$scope.rolelist=[];
	$http.post('/role/query',{"searchName":"会员"}).success(function (result) {
		if (result.got) {
            $scope.rolelist=result.data;
            $scope.formdata['role'] = $filter('getById')($scope.rolelist, $scope.formdata['role']);
        }
		
	 });
	
	

	$scope.update = function () {
        
		 var btn = $("#btnCreate");
	     btn.button('loading');
         $http.post('/fitnessmanages/modifyMember', $scope.formdata).success(function (result) {
        	 if (result.modified) {
                 $scope.AddSuccess = true;
                 window.location.href = "fitnessmanages#/member/management";
             }
        });
    }
	
}])

dashboard.controller('memberManagement', ['$scope', '$http','$route','selectMemberID',function($scope,$http,$route,selectMemberID){
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
		
		$scope.Modify = function (memberID) {
			selectMemberID.setString(memberID)
	        window.location.href = 'fitnessmanages#/member/management/modify';
	    };
	    
	    $scope.search= function (key){
	    	$scope.find={};
	    	$scope.find.PageNo=0
	    	$scope.find.searchKey=key;
	    	$http.post('/fitnessmanages/searchMember', $scope.find).success(function (result) {
	        	if (result.got) {
	        		$scope.memberlist = result.data;
	        		
	            }
	        });
	    }
		
	
	    $scope.init = function () {
			// App.init();
	    }
}])

