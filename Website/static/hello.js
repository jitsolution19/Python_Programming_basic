function sayHello() {
  alert("Hello World")
}

function total() {
  let sum = 0;
  const Collvalues = document.getElementsByName('tAmount');
  for (let i = 0; i < Collvalues.length; i++) {
    sum += parseFloat(Collvalues[i].value);
  }
  document.getElementById("amount").innerHTML = sum;
}

function addrow() {
  const trow = document.getElementsByName("output");
  const rowadd = trow.createElement("tr");
  const coladd = rowadd.createElement("td");
  const partxt = coladd.createElement("p");
  partxt.innerHTML = "Testing";
  coladd.appendChild(partxt);
  rowadd.appendChild(partxt);endChild(partxt);endChild(coladd);
  trow.appendChild(rowadd);
}

function addRecord() {

  // document.getElementById("getrec").appendChild(tableCreate());
  document.getElementById("getrec").innerHTML = "<table style='width=100%'><th>Date</th>" +
    "<th>S.no</th>" +
    "<th>Type</th>" +
    "<th>Description</th>" +
    "<th>Amount</th>" +
    "<tbody>" +
    "<tr><td>valeu2</td></tr>" +
    "</tbody>" +
    "</table>";
}

function tableCreate() {
  const body = document.body,
    tbl = document.createElement('table');
  tbl.style.width = '100px';
  tbl.style.border = '1px solid black';

  for (let i = 0; i < 3; i++) {
    const tr = tbl.insertRow();
    for (let j = 0; j < 2; j++) {
      if (i === 2 && j === 1) {
        break;
      } else {
        const td = tr.insertCell();
        td.appendChild(document.createTextNode(`Cell I${i}/J${j}`));
        td.style.border = '1px solid black';
        if (i === 1 && j === 1) {
          td.setAttribute('rowSpan', '2');
        }
      }
    }
  }
  body.appendChild(tbl);
}

