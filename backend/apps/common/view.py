from flask import Flask, jsonify, make_response


def not_request(error):
    """ View when is 400 error """
    return make_response(
        jsonify( 
            { 'error': 'Bad request' } 
        ), 
        400
    )


def not_found(error):
    """ View when is 404 error """
    return make_response(
        jsonify( 
            { 'error': 'Not found' } 
        ),
        404
    )


def not_allowed(error):
    """ View when is 405 error """
    return make_response(
        jsonify(
            { 'error': 'Method Not Allowed' } 
        ), 
        405
    )


def server_error(error):
    """ View when is 500 error """
    return make_response(
        jsonify(
            { 'error': 'Internal Server Error' } 
        ),
        500
    )
