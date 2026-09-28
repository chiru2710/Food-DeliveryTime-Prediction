const API =
  "https://food-deliverytime-prediction-7gph.onrender.com/predict";

const $ = (id) => document.getElementById(id);

$("form").addEventListener("submit", async (e) => {
  e.preventDefault();

  // Disable button while prediction is running
  $("btn").disabled = true;
  $("btn").firstChild.textContent = "Predicting...";

  // Hide previous error
  $("error").style.display = "none";

  // Collect form data
  const body = {
    distance: Number($("distance").value),
    weather: $("weather").value,
    traffic_level: $("traffic_level").value,
    time_of_day: $("time_of_day").value,
    vehicle_type: $("vehicle_type").value,
    preparation_time: Number($("preparation_time").value),
    courier_experience: Number($("courier_experience").value),
  };

  try {
    // Send request to FastAPI backend
    const response = await fetch(API, {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },

      body: JSON.stringify(body),
    });

    // Check HTTP response
    if (!response.ok) {
      let errorMessage = `API request failed (${response.status})`;

      try {
        const errorData = await response.json();

        if (errorData.detail) {
          errorMessage += `: ${errorData.detail}`;
        }
      } catch {
        // Ignore JSON parsing error
      }

      throw new Error(errorMessage);
    }

    // Convert response to JSON
    const data = await response.json();

    console.log("API Response:", data);

    // Get prediction from FastAPI response
    const prediction = Number(data.predicted_delivery_time);

    // Validate prediction
    if (!Number.isFinite(prediction)) {
      throw new Error(
        "Prediction field was not found in the API response."
      );
    }

    // Display prediction
    $("prediction").textContent = prediction.toFixed(2);

    // Display message
    if (prediction <= 35) {
      $("msg").textContent = "Fast delivery estimate.";
    } else if (prediction <= 60) {
      $("msg").textContent = "Moderate delivery time estimate.";
    } else {
      $("msg").textContent =
        "Longer delivery estimate — distance or traffic may be contributing.";
    }

    // Optional: show minutes explicitly
    if ($("unit")) {
      $("unit").textContent = "minutes";
    }

  } catch (error) {
    console.error("Prediction error:", error);

    $("error").textContent =
      "Prediction failed: " + error.message;

    $("error").style.display = "block";

  } finally {
    // Enable button again
    $("btn").disabled = false;

    $("btn").firstChild.textContent =
      "Predict Delivery Time ";
  }
});