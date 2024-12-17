document.querySelectorAll(".clickable-card").forEach(card => {
    card.addEventListener("click", async function (event) {
        event.preventDefault();

        if (this.querySelector("h3").textContent === "University Recommender") {
            // Collect user input
            const gpa = prompt("Enter your GPA (e.g., 3.9):");
            const gre = prompt("Enter your GRE Score (e.g., 320):");
            const interests = prompt("Enter your interests (e.g., Artificial Intelligence):");
            const budget = prompt("Enter your budget (in USD, e.g., 50000):");

            if (gpa && gre && interests && budget) {
                try {
                    const response = await fetch("http://127.0.0.1:7860/api/predict", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            data: [gpa, gre, interests, budget]
                        })
                    });

                    const result = await response.json();
                    alert(`Recommended University:\n${result.data[0]}`);
                } catch (error) {
                    console.error("Error:", error);
                    alert("Failed to get a recommendation. Please try again later.");
                }
            } else {
                alert("Please provide all the required inputs.");
            }
        }
    });
});
