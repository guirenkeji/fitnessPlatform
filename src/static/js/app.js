var dashboard = angular.module('dashboard', ['ngRoute']);

dashboard.run(['$rootScope', '$location', function($rootScope, $location) {

    $rootScope.$on('$routeChangeSuccess', function(newV) {
        $rootScope.path = $location.path();
        var path = $location.path().replace('/', '');
        console.log($rootScope.path);
        $rootScope.rootpath = path.slice(0, path.indexOf('/'));
        setTimeout(function () {
			// App.init();
			TableManageDefault.init();
		}, 200)
    });

}]);