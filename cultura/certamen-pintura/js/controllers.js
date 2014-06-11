'use strict';

/* Controllers */

var ajupegoControllers = angular.module('ajupegoControllers', []);

ajupegoControllers.controller('ResultatsController',
['$scope', '$http', '$routeParams' , function($scope, $http, $routeParams) {
    $http.get('http://localhost:8000/cultura/certamen-pintura/results.php').success(function(data) {
        $scope.certamen = data;

        $scope.edicio = $routeParams.edicio;

        console.log($scope);
    });
}]);