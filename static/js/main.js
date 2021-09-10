// function toggle for de modal
function toggleModal(modalID) {
    document.getElementById(modalID).classList.toggle("hidden");
    document.getElementById(modalID + "-backdrop").classList.toggle("hidden");
    document.getElementById(modalID).classList.toggle("flex");
    document.getElementById(modalID + "-backdrop").classList.toggle("flex");
}

// add style classes for the active link, where the user is browsing
function decorationLink() {

    let path = location.pathname

    let link = {
        '/app/patients': 'patients_link'
    }

    if (path != undefined) {
        element = document.getElementById(link[path])

        if (element != null) {
            element.classList.add('font-semibold')
        }
    }
}

(function () {
    decorationLink()
})();
