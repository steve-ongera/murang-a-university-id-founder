document.addEventListener("DOMContentLoaded", function () {
    function animateCount(element, start, end, duration) {
        let startTime = null;

        function updateCounter(currentTime) {
            if (!startTime) startTime = currentTime;
            let elapsedTime = currentTime - startTime;
            let progress = Math.min(elapsedTime / duration, 1);
            element.textContent = Math.floor(progress * (end - start) + start);
            
            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            }
        }

        requestAnimationFrame(updateCounter);
    }

    function startCounting() {
        let counters = document.querySelectorAll(".stat-counter");
        counters.forEach(counter => {
            let target = parseInt(counter.getAttribute("data-count"), 10);
            animateCount(counter, 0, target, 2000);
        });
    }

    // Check if the statistics section is visible
    function handleScroll() {
        let statsSection = document.getElementById("stats-section");
        if (statsSection) {
            let rect = statsSection.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom >= 0) {
                startCounting();
                window.removeEventListener("scroll", handleScroll); // Run only once
            }
        }
    }

    window.addEventListener("scroll", handleScroll);
    handleScroll(); // Run initially in case it's already in view
});
