'use strict'

describe 'Controller: TestRouteCtrl', ->

  # load the controller's module
  beforeEach module 'sandboxApp'

  TestRouteCtrl = {}
  scope = {}

  # Initialize the controller and a mock scope
  beforeEach inject ($controller, $rootScope) ->
    scope = $rootScope.$new()
    TestRouteCtrl = $controller 'TestRouteCtrl', {
      $scope: scope
    }

  it 'should attach a list of awesomeThings to the scope', ->
    expect(scope.awesomeThings.length).toBe 3
