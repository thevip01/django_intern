var c = document.getElementById('Languages').getElementsByTagName('input');
for (var i = 0; i < c.length; i++) {
    if (c[i].type == 'checkbox' || 'radio') {
        c[i].addEventListener('click', checkboxChecked)
    }
}
function checkboxChecked() {
    element = this
    if (element.checked == true) {
        element.value = element.name;

        console.log(element.name, document.getElementById(`read_${element.name}`));
        document.getElementById(`Beginner_${element.name}`).disabled = false;
        document.getElementById(`Mediator_${element.name}`).disabled = false;
        document.getElementById(`Expert_${element.name}`).disabled = false;

        document.getElementById(`read_${element.name}`).disabled = false;
        document.getElementById(`write_${element.name}`).disabled = false;
        document.getElementById(`speak_${element.name}`).disabled = false;
    }
    else {

        element.value = '';

        document.getElementById(`Beginner_${element.name}`).disabled = true;
        document.getElementById(`Mediator_${element.name}`).disabled = true;
        document.getElementById(`Expert_${element.name}`).disabled = true;

        document.getElementById(`read_${element.name}`).disabled = true;
        document.getElementById(`write_${element.name}`).disabled = true;
        document.getElementById(`speak_${element.name}`).disabled = true;
    }
}
let stateElement = document.getElementById('id_state')
stateElement.addEventListener('change', getcity)
let citySelect = document.getElementById('id_city')
async function getcity() {
    const state = stateElement.value;
    if (state != '') {
        fetch(`http://127.0.0.1:8000/job/getcity/${state}`, {
            method: 'get'
        })
            .then(res => res.json())
            .then(data => {
                let cities = data.cities;
                citySelect.innerHTML = '<option>---------</option>'
                for (let i in cities) {
                    option = document.createElement('option')
                    option.value = cities[i][2]
                    option.id = cities[i][0]
                    option.innerHTML = cities[i][2]
                    citySelect.appendChild(option)
                }
            })
    }
    else {
        citySelect.innerHTML = '<option>---------</option>'
    }
}


function AddForm(btn, FormID) {
    let btn_id = btn.id;
    let myform = document.getElementById(FormID)
    let node = myform.querySelector('.table')
    const clone = node.cloneNode(true);
    let Removebtn = clone.querySelector('li');
    clone.id = 'edu' + (Number(btn_id) + 1)
    Removebtn.id = Number(btn_id) + 1
    Removebtn.innerHTML = "Remove";
    Removebtn.setAttribute("onclick", `RemoveForm(this.id, ${FormID})`)
    myform.appendChild(clone);
    let input1 = clone.getElementsByTagName("input");
    for (let i = 0; i < input1.length; i++) {
        input1[i].value = "";
    }
    btn.id = Number(btn.id) + 1

}
function RemoveForm(btn_id, FormID) {
    education = document.getElementById(FormID)
    node = document.getElementById(`edu${btn_id}`)
    node.remove()
}