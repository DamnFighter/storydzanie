var tableRow = $("td").filter(function() {
    return $(this).text() == "Avg";
}).closest("tr");