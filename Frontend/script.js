const API = "https://food-deliverytime-prediction-7gph.onrender.com/predict";

const $ = (id) => document.getElementById(id);

$("form").addEventListener("submit", async (e) => {
  e.preventDefault();

  $("btn").disabled = true;
  $("btn").firstChild.textContent = "Predicting...";
  $("error").style.display = "none";

  const body = {
    distance: +$("distance").value,
    weather: $("weather").value,
    traffic_level: $("traffic_level").value,
    time_of_day: $("time_of_day").value,
    vehicle_type: $("vehicle_type").value,
    preparation_time: +$("preparation_time").value,
    courier_experience: +$("courier_experience").value,
  };

  try {
    const r = await fetch(API, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(body),
    });

    if (!r.ok) {
      throw new Error("API request failed (" + r.status + ")");
    }

    const d = await r.json();

    const v = Number(
      d.predicted_delivery_time ??
      d.delivery_time ??
      d.prediction ??
      d.estimated_delivery_time
    );

    if (!Number.isFinite(v)) {
      throw new Error("Prediction field was not found in the API response.");
    }

    $("prediction").textContent = v.toFixed(2);

    $("msg").textContent =
      v <= 35
        ? "Fast delivery estimate."
        : v <= 60
        ? "Moderate delivery time estimate."
        : "Longer delivery estimate — distance or traffic may be contributing.";

  } catch (err) {

    $("error").textContent = "Prediction failed: " + err.message;
    $("error").style.display = "block";

  } finally {

    $("btn").disabled = false;
    $("btn").firstChild.textContent = "Predict Delivery Time ";

  }
});