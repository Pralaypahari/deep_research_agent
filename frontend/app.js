const queryInput = document.getElementById("queryInput");
const output = document.getElementById("output");
const statusEl = document.getElementById("status");

document.getElementById("researchBtn").onclick = async () => {
  const query = queryInput.value.trim();
  if (!query) {
    statusEl.textContent = "Please enter a query";
    return;
  }

  statusEl.textContent = "Researching...";
  output.innerHTML = "";

  try {
    const res = await fetch("http://127.0.0.1:8000/research/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });

    const data = await res.json();
    statusEl.textContent = "Done";

    renderAnswer(data);
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Error";
    output.innerHTML = "<p>Something went wrong.</p>";
  }
};

document.getElementById("clearBtn").onclick = () => {
  queryInput.value = "";
  output.innerHTML = `<p class="placeholder">Results will appear here…</p>`;
  statusEl.textContent = "Idle";
};

function renderAnswer(data) {
  let html = `<h3>Query</h3><p>${data.query}</p><hr/>`;

  const answers = data.answers || {};

  for (const [section, text] of Object.entries(answers)) {
    html += `
      <h3>${section}</h3>
      ${formatText(text)}
    `;
  }

  output.innerHTML = html;
}

function formatText(text) {
  return `
    <div>
      ${text
        .replace(/^### (.*$)/gim, "<h4>$1</h4>")
        .replace(/^## (.*$)/gim, "<h3>$1</h3>")
        .replace(/^# (.*$)/gim, "<h2>$1</h2>")
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        .replace(/^- (.*$)/gim, "<li>$1</li>")
        .replace(/(<li>.*<\/li>)/gim, "<ul>$1</ul>")
        .replace(/\n{2,}/g, "</p><p>")
        .replace(/\n/g, "<br>")
      }
    </div>
  `;
}


