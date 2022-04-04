// replacing verification code
$(document).ready(function () {


    // save user updated wallet id in personal info content
    $('#save-wid-btn').click(function verify() {
        var input_wid = document.querySelector('#input-walletid').value;
        const regex = /^0x{1}[a-z\d]{64}$/;
        var valid_walletid;

        if (regex.test(input_wid) == true) {
            alert('Wallet id saved successfully');
            valid_walletid = input_wid;
            console.log(valid_walletid);
            $('#input-walletid')[0].placeholder = valid_walletid;
            // maybe don't use alert use some tooltip or something
        } else if (regex.test(input_wid) == false) {
            alert('Unvalid or empty wallet id entered!');
        };
    });

    // ---------------------- application form ----------------------

    // replacing verification code
    var geneCode = Math.floor(1000 + Math.random() * 9000); //generate new code
    console.log(geneCode);
    var veriCode = document.querySelector("#veri-code");
    console.log(veriCode);
    veriCode.textContent = geneCode;

    var nextBtn1 = $('#s1-nextBtn');
    var nextBtn2 = $('#s2-nextBtn');
    var nextBtn3 = $('#s3-nextBtn');

    var prevBtn2 = $('#s2-prevBtn');
    var prevBtn3 = $('#s3-prevBtn');
    var prevBtn4 = $('#s4-prevBtn');

    var step1 = $('#step-1');
    var step2 = $('#step-2');
    var step3 = $('#step-3');
    var step4 = $('#step-4');

    nextBtn1.on("click", function () {
        step1.css("left", "-570px");
        step2.css("left", "260px");
    })
    prevBtn2.on("click", function () {
        step2.css("left", "1110px");
        step1.css("left", "260px");
    })
    nextBtn2.on("click", function () {
        step2.css("left", "-570px");
        step3.css("left", "260px");
    })
    prevBtn3.on("click", function () {
        step2.css("left", "260px");
        step3.css("left", "1110px");
    })
    nextBtn3.on("click", function () {
        step3.css("left", "-570px");
        step4.css("left", "260px");
    })
    prevBtn3.on("click", function () {
        step2.css("left", "260px");
        step3.css("left", "1110px");
    })
    prevBtn4.on("click", function () {
        step3.css("left", "260px");
        step4.css("left", "1110px");
    })

    nextBtn1.css("pointerEvents", "none");
    // step 1 verification
    $('#veriBtn1').click(function () {

        var senderUsername = document.querySelector('#sender-username').value;
        var senderWallet = document.querySelector('#sender-wid').value;
        // this regex stands for: start with a single '0' along with a 'x', ends up with 64 (a-z)s/numbers
        const regex = /^0x{1}[a-z\d]{64}$/;

        // Multiplying by 9000 results in a range of [0, 9000).
        // Adding 1000 results in a range of [1000, 10000).
        // Flooring chops off the decimal value to give you an integer(讓結果是整數). Note that it does not round.(四捨五入)
        // var randNum = Math.floor(1000 + Math.random() * 9000);

        // not empty and pass the regex
        if (senderUsername != "" && senderWallet != "") {
            if (regex.test(senderWallet) == true) {
                nextBtn1.css("pointerEvents", "auto");
                alert('Verified.');
            } else if (regex.test(senderWallet) == false) {
                alert('Unvalid wallet id ! Please try again');
            }
        } else {
            alert('User name or wallet id is missing! Next button is disabled');
        }
    });


    nextBtn2.css("pointerEvents", "none");
    // step 2 verification
    $('#veriBtn2').click(function () {

        // var inputStr = input_recipiant_walletid;
        var receiWallet = document.querySelector('#recei-wid').value;
        const regex = /^0x{1}[a-zA-Z\d]{64}$/;
        // this regex stands for: start with a single '0' along with a 'x', ends up with 64 (a-z)s/numbers

        if (receiWallet != "") {
            if (regex.test(receiWallet) == true) {
                nextBtn2.css('pointerEvents', 'auto');
                alert('Wallet Id verified');
            } else if (regex.test(receiWallet) == false) {
                alert('Unvalid wallet id ! Next button is disabled');
            }
        }
        if (receiWallet == "") {
            alert('Missing recipiant wallet id !');
        }
    });

    $('#veriBtn3').click(function () {
        var inputCode = document.querySelector("#veriCode-input").value;
        console.log(inputCode);

        if (inputCode == geneCode) {
            $('#s3-nextBtn').css("pointerEvents", "auto");
            alert('Code verified !');
        } else if (inputCode != geneCode) {
            $('#s3-nextBtn').css("pointerEvents", "none");
            alert('Unvalid code !');
        } else {
            alert('Unmatched content entered !');
        }
    });

    nextBtn3.css("pointerEvents", "none");
    $('#s3-nextBtn').click(function () {

        var s1_senUsername = document.querySelector("#sender-username").value;
        var s1_senWid = document.querySelector("#sender-wid").value;
        var s1_senItem = document.querySelector("#sender-item");
        var s1_selected_item = s1_senItem.options[s1_senItem.selectedIndex].text;
        var s1_senNote = document.querySelector("#sender-notes").value;

        var s2_receiWid = document.querySelector("#recei-wid").value;
        var s2_receiNote = document.querySelector("#recei-notes").value;

        console.log(s1_senUsername, s1_senWid, s1_selected_item, s1_senNote);
        console.log(s2_receiWid, s2_receiNote);

        var s4_sen_username = document.querySelector("#s4-sender-username");
        var s4_sen_wid = document.querySelector("#s4-sender-wid");
        var s4_sen_itemNum = document.querySelector("#s4-sender-itemNum");
        var s4_sen_notes = document.querySelector("#s4-sender-notes");
        console.log(s4_sen_username, s4_sen_wid, s4_sen_itemNum, s4_sen_notes);

        var s4_recei_wid = document.querySelector("#s4-recei-wid");
        var s4_recei_notes = document.querySelector("#s4-recei-notes");
        console.log(s4_recei_wid, s4_recei_notes);

        s4_sen_username.textContent = s1_senUsername;
        s4_sen_wid.textContent = s1_senWid;
        s4_sen_itemNum.textContent = s1_selected_item;
        s4_sen_notes.textContent = s1_senNote;
        console.log(s4_sen_username, s4_sen_wid, s4_sen_itemNum, s4_sen_notes);

        s4_recei_wid.textContent = s2_receiWid;
        s4_recei_notes.textContent = s2_receiNote;
        console.log(s4_recei_wid, s4_recei_notes);
    });
});
