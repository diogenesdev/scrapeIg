function progressBar() {
    // Select the text and the width of the container
    var text = document.querySelector('.text')
    var container = getComputedStyle(document.querySelector('.container-bar')).width.replace('px', '')
        /**
         * Function call into a loop for using setTimeout method (for seeing the progression)  
         * Container width times 1 percent
         */
    for (var i = 0; i < container; i += container * .01) {
        tasks(i)
    }

    function tasks(i) {
        // setTimeout method with delay of 1 ms times i
        setTimeout(function() {
            // Stringify iterator i for writing css
            var val = JSON.stringify(i) + "px"
                // Modify css & text
            document.querySelector('.progress-bar').style.setProperty("width", val)
            text.textContent = Math.round((i / container) * 100) + "%"
        }, 1 * i)
    }
}

document.querySelector(".button").addEventListener("click", progressBar)