
async function linking(){
    var link = document.getElementById("link").value;
    var xd = await eel.linking(link)();
    console.log(xd);
    document.getElementById("resultado").value = xd;
}
