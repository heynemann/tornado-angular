'use strict'

###*
# @ngdoc overview
# @name sandboxApp
# @description
# # sandboxApp
#
# Main module of the application.
###
angular
  .module('sandboxApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config ($routeProvider, $locationProvider) ->
    $routeProvider
      .when '/',
        templateUrl: 'views/main.html'
        controller: 'MainCtrl'
      .when '/about',
        templateUrl: 'views/about.html'
        controller: 'AboutCtrl'
      .when '/test/route/view/with/many/paths',
        templateUrl: 'views/test-route.html'
        controller: 'TestRouteCtrl'

    $locationProvider.html5Mode(true)
