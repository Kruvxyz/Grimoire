// const express = require('express');
import express from 'express';
import bodyParser from 'body-parser'
import morgan from 'morgan';


const app = express();
const PORT = 3000;

// This middleware will log the request's hostname prefix  
// and allow it to proceed to the next handler
app.use(function (req, res, next) {
    console.log("Middleware called");
    const dotIndex = req.hostname.indexOf('.');
    if (dotIndex !== -1) {
        console.log(req.hostname.slice(0,req.hostname.indexOf('.')));
    } else {
        res.status(400).send('Invalid hostname');
    }
    next();
});
// Add poluare middleware
app.use(bodyParser.urlencoded({ extended: false }))
app.use(morgan('dev'));

// Requests will reach this route after 
// passing through the middleware
app.get('/user', function (req, res) {
    console.log("/user request called");
    res.send('Welcome to X');
});

// request with body-parser
app.post('/body', function (req, res) {
    console.log("/body POST request called");
    console.log(req.body);
    res.send('Welcome to X');
});

// Start the server
app.listen(PORT, function (err) {
    if (err) console.log(err);
    console.log(`Server listening on PORT ${PORT}`);
});