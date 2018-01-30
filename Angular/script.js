// script.js

// script.js

// Load Dependencies
var app = angular.module('mainApp', ['ngRoute']);

/*
function createCORSRequest(method, url) {
	var xhr = new XMLHttpRequest();
	console.log("CORS request called");
	if ("withCredentials" in xhr) {
		console.log("with credentials");
		xhr.open(method, url, true);
	} else {
		console.log("without credentials?D:");
		xhr = null;
	} return xhr;
}
*/

app.controller('mainController', function($scope) {} );

app.controller('homeController', function($scope, $http) {
               
              	$scope.name = "homeController";
		$scope.conjugations = "";
		
		$scope.conjugate = function() {
			if ($scope.verb != "") {
				console.log("Verb: " + $scope.verb);
				$http({
					url: '/conjugate',
					method: 'POST',
					headers: {'Content-Type' : 'application/json'},
					data: JSON.stringify({
						"verb" : $scope.verb
					})
				});
			}
		};
		

		//var url = "http://jisho.org/api/v1/search/words?keyword=oreo";
		/*
		$scope.conjugate = function() {
				.then(function(res) {
					$scope.conjugations = response.data;
				});
		}
		
		
		$scope.conjugate = function() {
			var xhr = createCORSRequest('GET', 'http://jisho.org/api/v1/search/words?keyword=oreo');
			xhr.send();
		}
		*/
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


