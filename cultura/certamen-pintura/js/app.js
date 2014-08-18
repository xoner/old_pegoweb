'use strict';

/* Application Module **/

var ajupegoApp = angular.module('ajupegoApp', [
    'ngRoute',
    'ajupegoControllers'
]);

ajupegoApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: 'partials/resultats.html',
                controller: 'ResultatsController'
            }).
            when('/:edicio', {
                templateUrl: 'partials/resultats.html',
                controller: 'ResultatsController'
            }).
            when('/:edicio/:obra', {
                templateUrl: 'partials/obra.html',
                controller: 'DetailsController'
            }).
            otherwise({
                redirectTo: '/'
            });
}]);