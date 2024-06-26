function deleteentry() {
    alert("jitendr");
    var text = document.getElementById("inputdata").value;
    //   console.log(text);
    document.getElementById("outputtext").innerText = text;
    alert(text);
};

/***********************************************************************************************************/
// Function   : Add Data in the Table 
// Table Name : ProductInventorys
// Date       : 02/06/2024
/***********************************************************************************************************/
$(function () {
    $("#addtext").click(function () {
        var text = document.getElementById("inputdata").value;
        console.log(text);
        alert("Add text--> " + text);
        $.ajax({
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ 'Purchase Date': text }),
            url: "/addOperation",
            success: function (response) {
                document.getElementById("outputtext").innerText = response;
            },
            error: function (xhr, status, error) {
                console.error("Error:", error);
            }
        });
    });
});

/***********************************************************************************************************/
// Function   : Display Data from the Table 
// Table Name : ProductInventorys
// Date       : 02/06/2024
/***********************************************************************************************************/
$(function () {
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
                        var itemHTML ="<li>";
                        for(var key in element){
                            // if(element.hasOwnProperty(key)){
                            //     itemHTML +=key + ":" + element[key]+",";
                            // }

                            if (element.hasOwnProperty(key)) {
                                itemHTML += "<strong>" + key + "</strong>: " + element[key] + "<br>";
                            }
                        }
                        itemHTML = itemHTML.slice(0, -2); // Remove the trailing comma and space
                        itemHTML += "</li>";
                        itemlist.insertAdjacentHTML("beforeend", itemHTML);

                        // var purchaseDate = element['Purchase date'];
                        // // var purchaseDate= element.Seller
                        // var id = element.id;
                        // itemlist.insertAdjacentHTML("beforeend", "<li>Purchase Date: " + purchaseDate + ", ID: " + id + "</li>");
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
/***********************************************************************************************************/
// ---------------------------------------------- End of Code ----------------------------------------------
/***********************************************************************************************************/