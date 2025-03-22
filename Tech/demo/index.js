document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("predictBtn").addEventListener("click", async () => {
    const userInfo = document.getElementById("userInfo").value;

    try {
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ userInfo }),
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data);
        document.getElementById("passChance").textContent = data.passChance;
        document.getElementById("missChance").textContent = data.missChance;
      } else {
        console.error("Error:", response.statusText);
      }
    } catch (error) {
      console.error("Fetch error:", error);
    }
  });

  document.getElementById("randomizeBtn").addEventListener("click", () => {
    const randomInfo = "Этот текст должен быть сгенерирован";
    document.getElementById("userInfo").value = randomInfo;
  });
});
