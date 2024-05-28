function addtext() {
    var text = document.getElementById("inputdata").value;
    console.log(text);
    document.getElementById("outputtext").innerText = text;
};

function updatetext() {

};

function deleteentry() {
    alert("jitendr");
    var text = document.getElementById("inputdata").value;
    //   console.log(text);
    document.getElementById("outputtext").innerText = text;
    alert(text);
};

function displayEntry() {
    alert("Display entry");
};

$(function(){
    $("#entry").click(function () {
        alert("Entry clicked");
        $.ajax({
            type: "GET",
            ContentType: "application/json",
            url: "/intro", success: function (results) {
                if (Array.isArray(results)) {
                    var itemlist = document.getElementById("dbdata");
                    itemlist.innerHTML = ""; 
                    results.forEach(function (element) {  
                        var purchaseDate = element["Purchase date"];
                        var id = element.id;
                        itemlist.insertAdjacentHTML("beforeend", "<li>Purchase Date: " + purchaseDate + ", ID: " + id + "</li>");
                    });
                } else {
                    console.error("Results is not an array");   
                }
            },
            error: function (xhr, status, error) {
                console.error("Error:", error);
            }

        });
    }); 
});

// $(document).ready(function () {
//     $("#entry").click(function () {
//         alert("Entry clicked");
//         $.ajax({
//             type: "GET",
//             ContentType: "application/json",
//             url: "/intro", success: function (results) {
//                 if (Array.isArray(results)) {
//                     results.forEach(function (element) {
//                         var itemlist = document.getElementById("dbdata");
//                         itemlist.insertAdjacentHTML("beforeend", "<li>"+element+"</li>");
//                     });
//                 } else {
//                     console.error("Results is not an array");
//                 }
//             },
//             error: function (xhr, status, error) {
//                 console.error("Error:", error);

//             }

//         });
//     });
// });
// document.querySelector("#addtext")
