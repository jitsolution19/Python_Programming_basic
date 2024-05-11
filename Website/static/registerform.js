$(document).ready(function(){

    $('#smartwizard').smartWizard({
            selected: 0,
            theme: 'arrows',
            autoAdjustHeight:true,
            transitionEffect:'fade',
            showStepURLhash: false,
         
    });

});

function  saveData(){
alert('Data Saved Successfully');
};