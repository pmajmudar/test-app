"use strict";

requirejs.config({
	// Default load from js/lib
	baseUrl: 'js/libs',
	// if it starts with src then use the src dir.
	// This is relative to the baseurl
	paths:{
		src:'../src',
		underscore:'underscore-min',
		backbone:'backbone-min',
		jquery:'jquery-1.11.0.min'
	}
});

requirejs(['jquery', 'underscore', 'backbone', 'src/doc_model'],
function($, _, Backbone, Model){
	
	// Create router with allowed routes
	var AppRouter = Backbone.Router.extend({
		routes:{
			'classify/:id':'classify',
			'*pages':'defaultRoute' /*match any uncaught urls */
		}
	});
	
	var app_router = new AppRouter;

	app_router.on('route:classify', function(id){
		console.log(id);
		console.log("I'm classifying!");
		var m = new Model({id:id});
		console.log(m.url());

		m.fetch({ success: function (m) {
					console.log(m);
				}
		});
	});
	
	app_router.on('route:defaultRoute', function(pages){
		console.log("In default");
		console.log(pages);
	});
	

	
	
	Backbone.history.start({pushState: true});
});