"use strict";requirejs(['jquery', 'underscore', 'backbone'],	function($, _, Backbone){	var ClassDoc = Backbone.Model.extend({		defaults:{			text: '',			classes: [],			duplicate: false		},				initialise: function(){			console.log("init");			}	});		return ClassDoc});