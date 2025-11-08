document.addEventListener('DOMContentLoaded', function() {
    // Clear form button functionality
    const clearButton = document.getElementById('clear-form');
    const form = document.querySelector('form');
    
    if (clearButton && form) {
        clearButton.addEventListener('click', function() {
            // Reset all form fields
            form.reset();
            
            // Uncheck all radio buttons (reset() doesn't always clear radio buttons properly)
            const radioButtons = form.querySelectorAll('input[type="radio"]');
            radioButtons.forEach(function(radio) {
                radio.checked = false;
            });
        });
    }
});
