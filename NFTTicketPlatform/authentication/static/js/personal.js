
// import $ from "jquery";

// open sidebar btn (1)
// const openBtn = document.querySelector("#open-btn");
// const closeBtn = document.querySelector("#close-btn");
// const sidebar = document.querySelector("#sidebar");

//(1)
// openBtn.onclick = () => {
//     sidebar.style.marginLeft = "0px";
//     openBtn.style.display = 'none';
//     closeBtn.style.display = 'block';
// };

// $('#open-btn').click(function () {
//     $('#sidebar').css('margin-left', '0px');
//     $('#open-btn').css('display', 'none');
//     $('#close-btn').css('display', 'block');
// });

// $('#close-btn').click(function () {
//     $('#sidebar').css('margin-left', '-200px');
//     $('#close-btn').css('display', 'none');
//     $('#open-btn').css('display', 'block');
// });

// closeBtn.onclick = () => {
//     sidebar.style.marginLeft = "-200px";
//     closeBtn.style.display = 'none';
//     openBtn.style.display = 'block';
// };

//--------------------------------------------------------------------------------------

// changing profile img
// const input_file = document.querySelector("#input-file");
// var uploaded_file = "";

// input_file.addEventListener("change", function () {
//     // console.log(input_file.value); // fakepath

//     const reader = new FileReader();
//     reader.addEventListener("load", () => {
//         uploaded_file = reader.result;
//         document.querySelector("#display-img").style.backgroundSize = "150px 150px";
//         document.querySelector("#display-img").style.backgroundImage = `url(${uploaded_file})`;
//     });
//     reader.readAsDataURL(this.files[0]);
// })

//--------------------------------------------------------------------------------------

//switch light to night
var light_switch = document.querySelector("#light-switch");
var night_switch = document.querySelector("#night-switch");
var main_bg = document.querySelector(".container-fluid");
var body = document.querySelector("BODY");

light_switch.onclick = () => {
    light_switch.style.display = 'none';
    night_switch.style.display = 'unset';
    light_switch.innerHTML = `<i class="fa-solid fa-moon"></i>`;
    main_bg.style.backgroundColor = 'white';
    body.style.color = 'black';
}
night_switch.onclick = () => {
    light_switch.style.display = 'unset';
    night_switch.style.display = 'none';
    light_switch.innerHTML = `<i class="fa-solid fa-circle-half-stroke"></i>`;
    main_bg.style.backgroundColor = '#222222';
    body.style.color = 'white';
}

//--------------------------------------------------------------------------------------

//switch visible to invisible
var invisible_switch = document.querySelector("#invisible-switch");
var visible_switch = document.querySelector("#visible-switch");
var number = document.querySelector(".b-num");
var number_innerText = document.querySelector(".b-num").innerText;

invisible_switch.onclick = () => {
    invisible_switch.style.display = 'none';
    visible_switch.style.display = 'unset';
    invisible_switch.innerHTML = `<i class="fa-solid fa-eye"></i>`;
    number.innerText = "***";
}
visible_switch.onclick = () => {
    visible_switch.style.display = 'none';
    invisible_switch.style.display = 'unset';
    visible_switch.innerHTML = `<i class="fa-solid fa-eye-slash"></i>`;
    number.innerText = number_innerText;
}

//--------------------------------------------------------------------------------------

// asset chart


//--------------------------------------------------------------------------------------

//--------------------------------------------------------------------------------------

// tp top btn
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

// ---------------------- application form ----------------------

//--------------------------------------------------------------------------------------

// $(document).ready(function () {


//     // save user updated wallet id in personal info content
//     $('#save-wid-btn').click(function verify() {
//         var input_wid = document.querySelector('#input-walletid').value;
//         const regex = /^0x{1}[a-z\d]{64}$/;
//         var valid_walletid;

//         if (regex.test(input_wid) == true) {
//             alert('Wallet id saved successfully');
//             valid_walletid = input_wid;
//             console.log(valid_walletid);
//             $('#input-walletid')[0].placeholder = valid_walletid;
//             // maybe don't use alert use some tooltip or something
//         } else if (regex.test(input_wid) == false) {
//             alert('Unvalid or empty wallet id entered!');
//         };
//     });


// });


// sum up collected data
