document.getElementById("sortButton").addEventListener("click", function() {
    // Get the input name from the user
    var name = document.getElementById("studentName").value;

    // Perform sorting hat logic
    var house = assignHouse(name);

    // Display the result
    document.getElementById("result").innerHTML = name + " belongs to " + house + "!";
});

function assignHouse(name) {
    // Simple hash function to assign house based on the name
    var hash = 0;
    for (var i = 0; i < name.length; i++) {
        hash += name.charCodeAt(i);
    }

    // Assign house based on the hash value
    var houseIndex = hash % 4;
    var houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"];
    return houses[houseIndex];
}
