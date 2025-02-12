document.addEventListener("DOMContentLoaded", function () {
    const searchBtn = document.getElementById("searchBtn");
    const searchInput = document.getElementById("searchInput");
    const searchResults = document.getElementById("searchResults");
    const searchModal = document.getElementById("searchModal");
    const closeModal = document.getElementById("closeModal");

    // Function to fetch results
    function fetchResults() {
        const query = searchInput.value.trim();
        if (query === "") {
            showMessage("Please enter a registration number or student name.", "text-red-500");
            return;
        }

        fetch(`/search-lost-ids/?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                searchResults.innerHTML = ""; // Clear previous results

                if (data.results.length > 0) {
                    data.results.forEach(id => {
                        searchResults.innerHTML += `
                            <div class="border p-3 rounded-md shadow-md flex items-center space-x-3 bg-gray-100">
                                <div>
                                    <p class="font-semibold text-gray-800">${id.student_name}</p>
                                    <p class="text-gray-600">${id.registration_number}</p>
                                    <span class="text-xs px-2 py-1 rounded-md text-white ${
                                        id.status === "FOUND" ? "bg-green-500" 
                                        : id.status === "CLAIMED" ? "bg-blue-500" 
                                        : "bg-yellow-500"
                                    }">
                                        ${id.status}
                                    </span>
                                </div>
                            </div>
                        `;
                    });

                    searchModal.classList.remove("hidden"); // Show modal
                } else {
                    showMessage("No matching ID found.", "text-gray-500");
                }
            })
            .catch(error => console.error("Error fetching data:", error));
    }

    // Search Button Click Event
    searchBtn.addEventListener("click", fetchResults);

    // Allow pressing Enter key for search
    searchInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            fetchResults();
        }
    });

    // Close Modal
    closeModal.addEventListener("click", function () {
        searchModal.classList.add("hidden"); // Hide modal
    });

    // Function to show messages
    function showMessage(message, color) {
        searchResults.innerHTML = `<p class="text-center ${color}">${message}</p>`;
        searchModal.classList.remove("hidden"); // Show modal with message
    }
});
