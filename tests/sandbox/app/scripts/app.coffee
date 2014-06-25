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
      .when '/web/',
        templateUrl: 'views/main.html'
        controller: 'MainCtrl'
      .when '/web/about',
        templateUrl: 'views/about.html'
        controller: 'AboutCtrl'
      .otherwise
        redirectTo: '/web/'

    $locationProvider.html5Mode(true)
