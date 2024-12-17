// Data for universities based on country selection
const universities = {
    usa: [
        "Harvard University",
        "Stanford University",
        "MIT",
        "California Institute of Technology"
    ],
    uk: [
        "University of Oxford",
        "University of Cambridge",
        "Imperial College London",
        "London School of Economics"
    ],
    australia: [
        "University of Sydney",
        "University of Melbourne",
        "Australian National University",
        "University of Queensland"
    ],
    canada: [
        "University of Toronto",
        "McGill University",
        "University of British Columbia",
        "University of Montreal"
    ]
};

// Real-time university update based on country selection
document.getElementById("country-select").addEventListener("change", function() {
    const country = this.value;
    const universityList = document.getElementById("university-list");
    universityList.innerHTML = "";  // Clear previous list

    if (country) {
        // Display the list of universities in real-time
        universities[country].forEach(function(university) {
            const li = document.createElement("li");
            li.textContent = university;
            universityList.appendChild(li);
        });
    }
});
