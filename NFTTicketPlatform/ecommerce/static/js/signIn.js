const passPersonal = document.querySelector("#personal-password");
const passCompany = document.querySelector("#enterprice-password");
const btnPersonal = document.querySelector(".visibility-toggle");
const btnCompany = document.querySelector("#show-pass");

console.log(btnPersonal.innerText);

btnPersonal.addEventListener("click", function () {
  if (passPersonal.type === "password") {
    passPersonal.type = "text";
    btnPersonal.innerText = "Hide Password";
  }
  else {
    passPersonal.type = "password";
    btnPersonal.innerText = "Show Password";
  }
});

btnCompany.addEventListener("click", function () {
  if (passCompany.type === "password") {
    passCompany.type = "text";
    btnCompany.innerText = "Hide Password";
  }
  else {
    passCompany.type = "password";
    btnCompany.innerText = "Show Password";
  }
});
