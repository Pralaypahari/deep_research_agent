function signup() {
  const email = document.getElementById("signupEmail").value;
  const password = document.getElementById("signupPassword").value;

  if (!email || !password) {
    alert("Please fill all fields");
    return;
  }

  localStorage.setItem("userEmail", email);
  localStorage.setItem("userPassword", password);

  alert("Account created successfully!");
  window.location.href = "login.html";
}

function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const savedEmail = localStorage.getItem("userEmail");
  const savedPassword = localStorage.getItem("userPassword");

  if (email === savedEmail && password === savedPassword) {
    window.location.href = "../index.html";
  } else {
    alert("Invalid email or password");
  }
}
