function getInputValue(){
    var domain = `${window.location.protocol}//${window.location.host}/`
    var inputVal = document.getElementById("search-input").value;
    window.location = `${domain}search/${inputVal}/`;
}