// showTable(data);

// d3.select('form').on('submit', handleSubmit);
// d3.select('button').on('click', handleSubmit);

// function showTable(data) {
//     d3.select('tbody').html('');
//     data.forEach(obj => {
//         var row = d3.select('tbody').append('tr');
//         Object.values(obj).forEach(val => {
//             var cell = row.append('td');
//             cell.text(val);
//         });
//     });
// };

// function handleSubmit() {
//     d3.event.preventDefault();
//     var filteredData = data;
//     var value = d3.select('input').property('value');
//     if (value){
//         filteredData=filteredData.filter(obj=>obj.datetime==value);
//     };
//     d3.select('input').node().value = "";
//     showTable(filteredData);
// };

// function processText() {
//     let text_file=document.getElementById("txt_file")
//     console.log(text_file[0])
// }

// function init(){
//     let text_file=document.getElementById('txt_file').addEventListener('change', handleFileSelect, false)
//     console.log(text_file[0])
// }
// function handleFileSelect(event){
//     const reader = new FileReader()
//     reader.onload = handleFileLoad;
//     reader.readAsText(event.target.files[0])
// }
function handleFileLoad(event){
    console.log(event);
    let fileContent=document.getElementById('textarea').textContent = event.target.result
    console.log(fileContent);
}

const fileSelector = document.getElementById('txt_file');
fileSelector.addEventListener('change', (event) => {
    const fileList = event.target.files;
    const reader = new FileReader()
    reader.onload = handleFileLoad;
    reader.readAsText(event.target.files[0])
    console.log(fileList);
});

function wordCount(val) {
    let wom = val.match(/\S+/g);
    return {
      charactersNoSpaces: val.replace(/\s+/g, '').length,
      characters: val.length,
      words: wom ? wom.length : 0,
      lines: val.split("\n").length,
      sentences: (val.split(/[.|!|?]+/g).length)-1,
      paragraphs: val.split(/\r?\n|\r/).length
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


// // Create Dropdown
// function init() {

//   var selector = d3.select("#selFunction");

//   d3.json("http://127.0.0.1:5000//api/v1.0/national_stats").then((data) => {
//     var careNames = []; 
//     data.forEach((datapoint) => {

//       careNames.push(datapoint["Value Code"])
    
//     });
//     careNames.forEach((care) => {
//       selector
//         .append("option")
//         .text(care)
//         .property("value", care);
//     });
  
//     const firstSample = careNames[0];
//     buildNationalSummary(firstSample);
//   });
// }

// // Event Listener
// function optionChanged(newCareType) {
//   panel = []
//   buildNationalSummary(newCareType);
// };

// init();