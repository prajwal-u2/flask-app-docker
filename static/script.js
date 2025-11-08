document.addEventListener('DOMContentLoaded', function() {
    const checkbox = document.getElementById('destination');
    const textareaSection = document.getElementById('dream_destination_section');
    
    function toggleTextarea() {
        if (checkbox.checked) {
            textareaSection.style.display = 'block';
        } else {
            textareaSection.style.display = 'none';
        }
    }
    
    toggleTextarea();
    
    checkbox.addEventListener('change', toggleTextarea);
});