const excelFilter = function(req, file, cb) {
    // Accept excel files only
    if (!file.originalname.match(/\.(xlsx|xls)$/)) {
        req.fileValidationError = 'Only Excel files are allowed!';
        return cb(new Error('Only Excel files are allowed!'), false);
    }
    cb(null, true);
};
exports.excelFilter = excelFilter;