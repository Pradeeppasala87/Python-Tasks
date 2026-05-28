document.addEventListener('DOMContentLoaded', () => {

    // 1. Button Ripple Animation
    const animBtns = document.querySelectorAll('.anim-btn');
    
    animBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            let x = e.clientX - e.target.getBoundingClientRect().left;
            let y = e.clientY - e.target.getBoundingClientRect().top;
            
            let ripples = document.createElement('span');
            ripples.style.left = x + 'px';
            ripples.style.top = y + 'px';
            ripples.classList.add('ripple');
            
            this.appendChild(ripples);
            
            setTimeout(() => {
                ripples.remove();
            }, 600);
        });
    });

    // 2. Right-Click Attendance Marking
    const attendanceBtns = document.querySelectorAll('.attendance-btn');
    
    attendanceBtns.forEach(btn => {
        btn.addEventListener('contextmenu', function(e) {
            e.preventDefault(); // Prevent default right-click menu
            
            // Toggle the 'marked-present' class
            if(this.classList.contains('marked-present')) {
                this.classList.remove('marked-present');
                this.textContent = 'Mark Present';
                // Here you would ideally trigger an AJAX request to update the backend
            } else {
                this.classList.add('marked-present');
                this.textContent = 'Present Marked';
                // Trigger animation by simulating a small bump
                this.style.transform = 'scale(1.05)';
                setTimeout(() => {
                    this.style.transform = 'scale(1)';
                }, 200);
                
                // Here you would trigger an AJAX request to update the backend
            }
        });
    });
});
