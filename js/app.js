showTable(data);

d3.select('form').on('submit', handleSubmit);
d3.select('button').on('click', handleSubmit);

function showTable(data) {
    d3.select('tbody').html('');
    data.forEach(obj => {
        var row = d3.select('tbody').append('tr');
        Object.values(obj).forEach(val => {
            var cell = row.append('td');
            cell.text(val);
        });
    });
};

function handleSubmit() {
    d3.event.preventDefault();
    var filteredData = data;
    var value = d3.select('input').property('value');
    if (value){
        filteredData=filteredData.filter(obj=>obj.datetime==value);
    };
    d3.select('input').node().value = "";
    showTable(filteredData);
};