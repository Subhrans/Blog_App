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
    autoProcessQueue: false,
    thumbnailWidth: 400,
    thumbnailHeight: 360,
    parallelUploads: 20,
    capture:'camera',
//    previewTemplate: previewTemplate,
//    createImageThumbnails: false,
    acceptedFiles:'.png, .jpg',
//    autoProcessQueue: false
    init: function(){
    this.on('complete',function(){

        location.reload();
    });
    this.on("addedfile", function(file) { alert("Added file."); });
   }
})
document.getElementById("submit-dropzone-btn-cover").addEventListener('click',function(e){
    e.preventDefault();
    myDropzone_cover.processQueue();
})
//$("#submit-dropzone-btn").click(function(){
//  myDropzone_cover.processQueue();
//});