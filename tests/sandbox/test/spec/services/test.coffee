'use strict'

describe 'Service: test', ->

  # load the service's module
  beforeEach module 'sandboxApp'

  # instantiate service
  test = {}
  beforeEach inject (_test_) ->
    test = _test_

  it 'should do something', ->
    expect(!!test).toBe true
