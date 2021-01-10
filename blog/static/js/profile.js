Dropzone.autoDiscover = false;

const myDropzone_profile = new Dropzone('#my-dropzone-profile',{
    maxFiles:1,
    dictDefaultMessage : 'Edit',
    addRemoveLinks: true,   // Add file remove button.
    acceptedFiles: '.jpg, .png',
    init: function () {
        // Set up any event handlers
        this.on('complete', function () {
            location.reload();
        });

    }

})

// Cover pic of dropzone

const myDropzone_cover = new Dropzone('#my-dropzone-cover',{
    maxFiles:1,
    dictDefaultMessage:"Edit",
    addRemoveLinks: true,
    createImageThumbnails: false,
    acceptedFiles:'.png, .jpg',
    init: function(){
    this.on('complete',function(){
        location.reload();
    });
   }
})