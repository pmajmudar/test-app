"use strict";

requirejs.config({
	// Default load from js/lib
	baseUrl: 'app/js/libs',
	// if it starts with app then use the app dir.
	// This is relative to the baseurl
	paths:{
		app:'../src',
		underscore:'underscore-min',
		backbone:'backbone-min'
	}
});

requirejs(['underscore', 'backbone', 'app/model'],
function(_, Backbone, model){
	// app model is loaded?
	var AppRouter = Backbone.Router.extend({
		routes:{
			'/search':
		}
	});
	
});