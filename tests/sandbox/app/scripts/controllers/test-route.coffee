'use strict'

###*
 # @ngdoc function
 # @name sandboxApp.controller:TestRouteCtrl
 # @description
 # # TestRouteCtrl
 # Controller of the sandboxApp
###
angular.module('sandboxApp')
  .controller 'TestRouteCtrl', ($scope) ->
    $scope.awesomeThings = [
      'HTML5 Boilerplate'
      'AngularJS'
      'Karma'
    ]
