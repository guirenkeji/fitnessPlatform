dashboard.controller('sidebar', ['$scope', '$rootScope', function($scope, $rootScope){

	$scope.init = function () {
		// App.init();
		console.log($rootScope.path);
	}
}])