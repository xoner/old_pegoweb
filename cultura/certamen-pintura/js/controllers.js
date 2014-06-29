'use strict';

/* Controllers */

var ajupegoControllers = angular.module('ajupegoControllers', []);

ajupegoControllers.controller('ResultatsController',
['$scope', '$http', '$routeParams' , function($scope, $http, $routeParams) {
    $http.get('/cultura/certamen-pintura/results.php?edicio=' + $routeParams.edicio).success(function(data) {
        $scope.certamen = data;

        $scope.edicio = $routeParams.edicio.toUpperCase();

        console.log($scope);
    });
}]);