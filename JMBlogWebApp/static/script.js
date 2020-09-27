var element = document.getElementById('RemoveBtId');

function OnRemoveClick() {
    var userSelection = confirm("Are you sure?")
    return (userSelection ? true : false);
}
