// script.js

// script.js

// Load Dependencies
var app = angular.module('mainApp', ['ngRoute']);

app.controller('mainController', function($scope) {} );

app.controller('homeController', function($scope, $http) {
               
              	$scope.name = "homeController";
		$scope.conjugations = "";
		$scope.conjugate = function() {
			if ($scope.verb != "") {
				console.log("Verb: " + $scope.verb);
			}
		}

               });

app.controller('aboutController', function($scope, $http) {
               
               
               });

app.controller('contactController', function($scope, $http) {
               
               $scope.name = "contactController";
               });



app.config(function($routeProvider, $locationProvider) {
           
    $routeProvider
    
           .when('/', {
                 
                 templateUrl: 'template/conjugate.html',
                 controller: 'homeController'
            })
           
           .when('/about', {
                 
                 templateUrl: 'template/about.html',
                 controller: 'aboutController'
            })
           
           .when('/contact', {
                 
                 templateUrl: 'template/contact.html',
                 controller: 'contactController'
            })

           .when('/error404', {
                 
                 templateUrl: 'template/404.html',
                 controller: 'error404Controller'
            })
           
           .otherwise({
           
                      redirectTo: '/'
           });
           
           $locationProvider.html5Mode(true);
});


