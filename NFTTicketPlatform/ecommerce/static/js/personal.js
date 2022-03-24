
// open sidebar btn
const openBtn = document.querySelector("#open-btn");
const closeBtn = document.querySelector("#close-btn");
const sidebar = document.querySelector("#sidebar");

// sidebar tabs
const tab_info = document.querySelector("#tab-info");
const tab_asset = document.querySelector("#tab-asset");
const tab_help = document.querySelector("#tab-info");

// display panels
const pane_info = document.querySelector("#pane-info");
const pane_asset = document.querySelector("#pane-asset");
const pane_help = document.querySelector("#pane-help");

// console.log(pane_info);
// console.log(pane_asset);
// console.log(pane_help);

openBtn.onclick = () => {
    sidebar.style.marginLeft = "0px";
    openBtn.style.display = 'none';
    openBtn.innerText = "Close Sidebar";
    closeBtn.style.display = 'block';
};

closeBtn.onclick = () => {
    sidebar.style.marginLeft = "-250px";
    closeBtn.style.display = 'none';
    openBtn.style.display = 'block';
    openBtn.innerText = "Open Sidebar";
    openBtn.innerHTML = `
    <i class="fas fa-align-left"></i>
    <span>Open Sidebar</span>
    `;
};

function show_Info() {
    pane_info.style.display = 'unset';
    pane_asset.style.display = 'none';
    pane_help.style.display = 'none';
    // pane_asset.style.transition = "0.5s";
}

function show_Asset() {
    pane_info.style.display = 'none';
    pane_asset.style.display = 'unset';
    pane_help.style.display = 'none';
}

function show_Help() {
    pane_info.style.display = 'none';
    pane_asset.style.display = 'none';
    pane_help.style.display = 'unset';
}
