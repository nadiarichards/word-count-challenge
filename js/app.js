function init(){
    let text_file=document.getElementById('txt_file').addEventListener('change', handleFileSelect, false)
    console.log(text_file[0])
}
function handleFileSelect(event){
    const reader = new FileReader()
    reader.onload = handleFileLoad;
    reader.readAsText(event.target.files[0])
}
function handleFileLoad(event){
    console.log(event);
    document.getElementById('fileContent').textContent = event.target.result;
}