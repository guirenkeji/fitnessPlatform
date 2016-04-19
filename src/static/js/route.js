dashboard.config(['$routeProvider',function ($routeProvider) {
    $routeProvider
    .when('/user/management', {
        templateUrl: '/static/views/user/management.html',
        controller: 'userManagement'
    })
    .when('/user/management/add', {
        templateUrl: '/static/views/user/add.html',
        controller: 'userAdd'
    })
    .when('/user/competence', {
        templateUrl: '/static/views/user/competence.html',
        controller: 'userCompetence'
    })

    .when('/personnel/management', {
        templateUrl: '/static/views/personnel/management.html',
        controller: 'personnelManagement'
    })
    .when('/personnel/management/add', {
        templateUrl: '/static/views/personnel/add.html',
        controller: 'personnelAdd'
    })

    .when('/member/management', {
        templateUrl: '/static/views/member/management.html',
        controller: 'memberManagement'
    })
    .when('/member/management/add', {
        templateUrl: '/static/views/member/add.html',
        controller: 'memberAdd'
    })

    .when('/commodity/management', {
        templateUrl: '/static/views/commodity/management.html',
        controller: 'commodityManagement'
    })
    .when('/commodity/management/add', {
        templateUrl: '/static/views/commodity/add.html',
        controller: 'commodityAdd'
    })

    .when('/courses/team/management', {
        templateUrl: '/static/views/teamCourses/management.html',
        controller: 'teamCoursesManagement'
    })
    .when('/courses/team/management/add', {
        templateUrl: '/static/views/teamCourses/add.html',
        controller: 'teamCoursesAdd'
    })

    .when('/courses/private/management', {
        templateUrl: '/static/views/privateCourses/management.html',
        controller: 'privateCoursesManagement'
    })
    .when('/courses/private/management/add', {
        templateUrl: '/static/views/privateCourses/add.html',
        controller: 'privateCoursesAdd'
    })
    
    .otherwise({
        redirectTo: '/user/management'
    });
}]);