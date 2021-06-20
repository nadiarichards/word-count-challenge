// function handleFileLoad(event){
//     console.log(event);
//     let fileContent=document.getElementById('textarea').textContent = event.target.result
//     console.log(fileContent);
// }

// const fileSelector = document.getElementById('txt_file');
// fileSelector.addEventListener('change', (event) => {
//     const fileList = event.target.files;
//     const reader = new FileReader()
//     reader.onload = handleFileLoad;
//     reader.readAsText(event.target.files[0])
//     console.log(fileList);
// });

function wordCount(val) {
    let wom = val.match(/\S+/g);
    return {
      charactersNoSpaces: val.replace(/\s+/g, '').length,
      characters: val.length,
      words: wom ? wom.length : 0,
      lines: val.split(/\r*\n/).length,
      sentences: val.split(/[.|!|?]+/g).length,
      paragraphs: val.split("\n\n").length
    };
  }

let textarea = document.getElementById('textarea');
let result = document.getElementById('result');
  
textarea.addEventListener('input', function() {
    let wc = wordCount(this.value);
    result.innerHTML = (`
    <br><strong>Characters without spaces:</strong>  ${wc.charactersNoSpaces}
    <br><strong>Characters with spaces:</strong>  ${wc.characters}
    <br><strong>Words:</strong>  ${wc.words}
    <br><strong>Lines:</strong>  ${wc.lines}
    <br><strong>Paragraphs:</strong>  ${wc.paragraphs}
    <br><strong>Sentences:</strong>  ${wc.sentences}
    `);
  });