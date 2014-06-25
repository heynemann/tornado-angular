'use strict'

###*
 # @ngdoc service
 # @name sandboxApp.test
 # @description
 # # test
 # Factory in the sandboxApp.
###
angular.module('sandboxApp')
  .factory 'test', ->
    # Service logic
    # ...

    meaningOfLife = 42

    # Public API here
    {
      someMethod: ->
        meaningOfLife
    }
