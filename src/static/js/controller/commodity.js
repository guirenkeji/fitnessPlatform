// 健身器材
dashboard.controller('commodityManagement', ['$scope', function($scope){

    $scope.init = function () {
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

dashboard.controller('commodityAdd', ['$scope','$http', function($scope,$http){
    $scope.init = function () {
        FormPlugins.init();
    }
//    $scope.order = {}
    $scope.create = function () {
        $http.post('/order/fitnessorder/add', $scope.order).success(function (result) {
        	if (result.created) {
                alert("Success");
                window.location.href = 'fitnessmanages#/commodity/record'
            }
        });
    }
}])
//记录查询
dashboard.controller('commodityRecord', ['$scope','$http',function($scope,$http){
	$scope.Query = { PageNo: 1, role: ''};
    $scope.init = function () {
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
        $http.post('/order/fitnessorder/query', $scope.Query).success(function (result) {
            btn.button('reset');
            $scope.OrderList = result.data;
          
         
        });
    }    
}])