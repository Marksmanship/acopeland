process.title = "node-website-template";

// core module
var http = require('http');

// npm packages
var ErrorPage = require('error-page');
var Templar = require('templar');
var router = require('routes')();

var environment = process.env.NODE_ENV || 'development';
var config = require('./config/' + environment + '.js');
var templarOptions = { engine: config.engine, folder: config.templates };

