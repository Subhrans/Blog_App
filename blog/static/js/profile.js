Dropzone.autoDiscover = false;

const myDropzone = new Dropzone('#my-dropzone',{
    maxFiles:1,
    maxFileSize:2,
    addRemoveLinks: true,   // Add file remove button.
    acceptedFiles: '.jpg, .png',
    init: function () {
        // Set up any event handlers
        this.on('complete', function () {
            location.reload();
        });

    }

})