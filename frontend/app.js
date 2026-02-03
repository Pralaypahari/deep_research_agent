const q = document.getElementById("queryInput");
const out = document.getElementById("output");
const status = document.getElementById("status");

document.getElementById("researchBtn").onclick = async () => {
  if (!q.value.trim()) return status.textContent = "Enter a query";

  status.textContent = "Researching...";
  out.innerHTML = "";

  try {
    const res = await fetch("http://localhost:8000/research", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query: q.value,
        use_web: useWeb.checked,
        use_docs: useDocs.checked
      })
    });

    const data = await res.json();
    status.textContent = "Done";

    out.innerHTML = `
      <b>Plan</b><p>${data.plan || ""}</p>
      <b>Research</b><p>${data.research || ""}</p>
      <b>Final Answer</b><p>${data.final_answer || ""}</p>
    `;
  } catch (e) {
    status.textContent = "Error";
    out.innerHTML = "Something went wrong";
  }
};

document.getElementById("clearBtn").onclick = () => {
  q.value = "";
  out.innerHTML = "";
  status.textContent = "Idle";
};
