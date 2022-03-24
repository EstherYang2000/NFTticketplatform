$(document).ready(function () {
    // jQuery methods go here...\

    // open sidebar
    $('#open-btn').click(function (e) {
        e.preventDefault();
        $('#sidebar').css('margin-left', '0px');
        $('#open-btn').css('display', 'none');
        $('#open-btn').text('Close Sidebar');
        $('#close-btn').css('display', 'block');
    });

    // close sidebar
    $('#close-btn').click(function (e) {
        e.preventDefault();
        $('#sidebar').css('margin-left', '-250px');
        $('#close-btn').css('display', 'none');
        $('#open-btn').css('display', 'block');
        $('#open-btn').text('Open Sidebar');
        $('#open-btn').html(`<i class="fas fa-align-left"></i>
        <span>Open Sidebar</span>`);
    });

    // 顯示公司資訊
    $('#tab-info').click(function (e) {
        e.preventDefault();//阻止此元素預設動作
        $('#pane-info').show();
        $('#pane-activity').hide();
        $('#pane-asset').hide();
        $('#pane-sell').hide();
        $('#pane-help').hide();
    });
    $('#tab-info').click();//頁面載入時預先觸發

    // 顯示公司資產
    $('#tab-asset').click(function (e) {
        e.preventDefault();//阻止此元素預設動作        
        $('#pane-asset').show();
        $('#pane-info').hide();
        $('#pane-activity').hide();
        $('#pane-sell').hide();
        $('#pane-help').hide();
    });

    // 顯示新增活動
    $('#tab-activity').click(function (e) {
        e.preventDefault();//阻止此元素預設動作
        $('#pane-activity').show();
        $('#pane-info').hide();
        $('#pane-asset').hide();
        $('#pane-sell').hide();
        $('#pane-help').hide();
    });

    // 顯示銷售狀況
    $('#tab-sell').click(function (e) {
        e.preventDefault();//阻止此元素預設動作
        $('#pane-sell').show();
        $('#pane-info').hide();
        $('#pane-asset').hide();
        $('#pane-activity').hide();
        $('#pane-help').hide();
    });

    // 顯示詢問中心
    $('#tab-help').click(function (e) {
        e.preventDefault();//阻止此元素預設動作        
        $('#pane-help').show();
        $('#pane-asset').hide();
        $('#pane-info').hide();
        $('#pane-activity').hide();
        $('#pane-sell').hide();
    });

    // 銷售狀況x軸票名，y軸銷售票數
    var xValues = ["A票", "B票", "C票", "D票", "E票"];//票名
    var yValues = [55, 49, 44, 24, 20];//票名對應的銷售票數
    var barColors = new Array();

    for (let index = 0; index < xValues.length; index++) {
        barColors.push(getRandomColor());
    }

    new Chart("myChart", {
        type: "bar",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: barColors,
                data: yValues
            }]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: "World Wine Production 2018"
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });

    function getRandomColor() {
        var letters = '0123456789ABCDEF'.split('');
        var color = '#';
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }

    $('#amazing-colorful-card-columns > .card').each(function (index, element) {
        // element == this
        $(element).css({
            'background-color': getRandomColor(),
            'color': 'white'
        });
    });
    $('#amazing-colorful-card-columns > .card').hover(function () {
        // over
        $(this).css({
            'background-color': 'white',
            'color': 'black'
        });
    }, function () {
        // out
        $(this).css({
            'background-color': getRandomColor(),
            'color': 'white'
        });
    }
    );
});

// open sidebar btn
// const openBtn = document.querySelector("#open-btn");
// const closeBtn = document.querySelector("#close-btn");
// const sidebar = document.querySelector("#sidebar");

// sidebar tabs
// const tab_info = document.querySelector("#tab-info");
// const tab_asset = document.querySelector("#tab-asset");
// const tab_help = document.querySelector("#tab-info");

// display panels
// const pane_info = document.querySelector("#pane-info");
// const pane_asset = document.querySelector("#pane-asset");
// const pane_help = document.querySelector("#pane-help");

// console.log(pane_info);
// console.log(pane_asset);
// console.log(pane_help);

// openBtn.onclick = () => {
//     sidebar.style.marginLeft = "0px";
//     openBtn.style.display = 'none';
//     openBtn.innerText = "Close Sidebar";
//     closeBtn.style.display = 'block';
// };

// closeBtn.onclick = () => {
//     sidebar.style.marginLeft = "-250px";
//     closeBtn.style.display = 'none';
//     openBtn.style.display = 'block';
//     openBtn.innerText = "Open Sidebar";
//     openBtn.innerHTML = `
//     <i class="fas fa-align-left"></i>
//     <span>Open Sidebar</span>
//     `;
// };

// function show_Info() {
//     pane_info.style.display = 'unset';
//     pane_asset.style.display = 'none';
//     pane_help.style.display = 'none';
//     // pane_asset.style.transition = "0.5s";
// }

// function show_Asset() {
//     pane_info.style.display = 'none';
//     pane_asset.style.display = 'unset';
//     pane_help.style.display = 'none';
// }

// function show_Help() {
//     pane_info.style.display = 'none';
//     pane_asset.style.display = 'none';
//     pane_help.style.display = 'unset';
// }

