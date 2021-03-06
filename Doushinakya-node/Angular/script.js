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
		$scope.dic = "";
		$scope.eng = "";
		$scope.type = "";
		$scope.masu = "";
		$scope.nai = "";
		$scope.te = "";
		$scope.pot = "";
		$scope.vol = "";
		
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
				})
				.then(function successCallBack(response) {
					console.log("then function");
					//console.log(Object.prototype.toString.call(JSON.parse(response.data)));	
					console.log(eval("(" + response.data + ")"));	
					var obj = eval("(" + response.data + ")");	
					$scope.dic = "Dictionary Form: " + obj['Dictionary Form'];
					$scope.eng = "English: " + obj['English Definition'];
					$scope.type = "Type: " + obj['Type'];
					$scope.masu = "Masu Form: " + obj['Masu'];
					$scope.nai = "Negative (Nai) Form: " + obj['Nai'];
					$scope.te = "Te Form: " + obj['Te'];
					$scope.pot = "Potential Form: " + obj['Potential'];
					$scope.vol = "Volitional Form: " + obj['Volitional'];
				}
				, function errCallBack(response) {
					console.log("Error");
				});
				//$http.post('/conjugate');
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


