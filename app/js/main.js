"use strict";

requirejs.config({
	// Default load from js/lib
	baseUrl: 'app/js/libs',
	// if it starts with src then use the src dir.
	// This is relative to the baseurl
	paths:{
		src:'../src',
		underscore:'underscore-min',
		backbone:'backbone-min',
		jquery:'jquery-1.11.0.min'
	}
});

requirejs(['jquery', 'underscore', 'backbone', 'src/model'],
function($, _, Backbone, model){
	
	// Create router with allowed routes
	var AppRouter = Backbone.Router.extend({
		routes:{
			'search':'search',
			'*pages':'defaultRoute' /*match any uncaught urls */
		}
	});
	
	var app_router = new AppRouter;

	app_router.on('route:search', function(){
		var anything;
		console.log("I'm searching!");
	});
	
	app_router.on('route:defaultRoute', function(pages){
		console.log("In default");
		console.log(pages);
	});
	
	Backbone.history.start({pushState: true});
});