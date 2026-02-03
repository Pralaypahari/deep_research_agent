const q = document.getElementById("queryInput");
const out = document.getElementById("output");
const status = document.getElementById("status");

document.getElementById("researchBtn").onclick = async () => {
  if (!q.value.trim()) return status.textContent = "Enter a query";

  status.textContent = "Researching...";
  out.innerHTML = "";

  try {
    const res = await fetch("http://localhost:8000/research/query", {
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
      <b>query</b><p>${data.query || ""}</p>
      <b>status</b><p>${data.summary || ""}</p>
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
