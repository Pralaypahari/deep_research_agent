function signup() {
  const email = document.getElementById("signupEmail").value;
  const password = document.getElementById("signupPassword").value;

  if (!email || !password) {
    alert("Fill all fields");
    return;
  }

  localStorage.setItem("email", email);
  localStorage.setItem("password", password);

  alert("Account created successfully");
  window.location.href = "login.html";
}

function login() {
  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;

  const savedEmail = localStorage.getItem("email");
  const savedPassword = localStorage.getItem("password");

  if (email === savedEmail && password === savedPassword) {
    localStorage.setItem("isLoggedIn", "true");
    window.location.href = "../index.html";
  } else {
    alert("Invalid credentials");
  }
}
