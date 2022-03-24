
// -------------------------- pwd show/hide --------------------------

const passPersonal = document.querySelector("#personal-password");
const passEnterprice = document.querySelector("#enterprice-password");
const rePassPersonal = document.querySelector("#personal-repassword");
const rePassEnterprice = document.querySelector("#enterprice-repassword");
const btnPersonal = document.querySelector(".visibility-toggle");
const btnEnterprice = document.querySelector("#show-password");



btnPersonal.addEventListener("click", function () {
  if (passPersonal.type === "password") {
    passPersonal.type = "text";
    rePassPersonal.type = "text";
    btnPersonal.innerText = "Hide Password";
  }
  else {
    passPersonal.type = "password";
    rePassPersonal.type = "password";
    btnPersonal.innerText = "Show Password";
  }
});

btnEnterprice.addEventListener("click", function () {
  if (passEnterprice.type === "password") {
    passEnterprice.type = "text";
    rePassEnterprice.type = "text";
    btnEnterprice.innerText = "Hide Password";
  }
  else {
    passEnterprice.type = "password";
    rePassEnterprice.type = "password";
    btnEnterprice.innerText = "Show Password";
  }
});



// -------------------------- end pwd show/hide --------------------------


//-------------------------- sign up success jump --------------------------
// function authentication() {
  // var personal_userName = document.querySelector("#personal-userName").value;
  // var personal_email = document.querySelector("#personal-email").value;
  // var personal_pass = document.querySelector("#personal-pass").value;
  // var personal_walletId = document.querySelector("#personal-walletId").value;

  // console.log(personal_userName);
  // alert(personal_userName + '\n' + personal_email + '\n' + personal_pass + '\n' + personal_walletId);



//-------------------------- end sign up success jump --------------------------