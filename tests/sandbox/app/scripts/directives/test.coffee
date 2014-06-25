'use strict'

###*
 # @ngdoc directive
 # @name sandboxApp.directive:test
 # @description
 # # test
###
angular.module('sandboxApp')
  .directive('test', ->
    template: '<div></div>'
    restrict: 'E'
    link: (scope, element, attrs) ->
      element.text 'this is the test directive'
  )
