dashboard.config(['$routeProvider',function ($routeProvider) {
    $routeProvider
    .when('/iso/list', {
        templateUrl: 'views/iso/list.html',
        controller: 'isoList'
    })
    .when('/iso/make', {
        templateUrl: 'views/iso/make.html',
        controller: 'isoMake'
    })
    .when('/app/create', {
        templateUrl: 'views/app/create.html',
        controller: 'appCreate'
    })
    .when('/app/status', {
        templateUrl: 'views/app/status.html',
        controller: 'appStatus'
    })
    .otherwise({
        redirectTo: '/iso/list'
    });
}]);

