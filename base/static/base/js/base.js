// Smooth Scroll for links
document.addEventListener('DOMContentLoaded', function () {
    // Smooth Scroll for hash links (kept minimal)
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function (e) {
            var target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});

