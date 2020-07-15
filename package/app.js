const express = require('express')
const ejs = require('ejs');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const helpers = require('./helpers');

const app = express()

app.set('views', './views');
app.set('view engine', 'ejs');
app.use(express.urlencoded({extended: false}));
app.use(express.static(__dirname + '/public'));

app.get('/', (req, res) => {
    res.render("index");
});

const storage = multer.diskStorage({
    destination: function(req, file, cb) {
        cb(null, './uploads/');
    },

    // By default, multer removes file extensions so let's add them back
    filename: function(req, file, cb) {
        cb(null, file.originalname);
    }
});

app.post('/', (req, res) => {

    let upload = multer({ storage: storage, fileFilter: helpers.excelFilter }).single('excel_file');

    upload(req, res, function(err) {
        // req.file contains information of uploaded file
        // req.body contains information of text fields, if there were any

        if (req.fileValidationError) {
            //Render message
            console.log(1);
            return res.send(req.fileValidationError);
        }
        else if (!req.file) {
            //Render message
            console.log(2);
            return res.send('Please select an excel file to upload. Will you? Please?');
        }
        else if (err instanceof multer.MulterError) {
            // Render message
            console.log(3);
            return res.send(err);
        }
        else if (err) {
            console.log(4);
            return res.send(err);
        }
        
        const { spawn } = require('child_process');
        const pyProg = spawn('python', ['./python_script/MAin.py', `./uploads/${req.file.originalname}`]);
        
        pyProg.stderr.once('data', (data) => {
            // console.log(data);
            res.send(`Sorry, an error occured in python: ${data}`);
        });

        pyProg.stdout.on('data', function(data) {
            res.sendFile('./result.xlsx', {root: __dirname}, (err) => {
                fs.unlink('./result.xlsx', () => {});
            });
        });

    });
    
});

app.listen(process.env.PORT || 4000, () => console.log('Application listening on port 4000!'))