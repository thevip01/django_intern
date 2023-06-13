document.getElementsByTagName('body')[0].addEventListener('onload', getFunction())
async function getFunction() {
    id = document.getElementById('nonematter').value
    if (id != '') {
        let response = await fetch('http://127.0.0.1:8000/job/getData/' + id)
        let DataSet = await response.json()
        let Data = DataSet['Data']
        let Languages = DataSet['Language']
        let MultiData = DataSet['MultipleData']
        let fields = ['BasicData', 'PreferenceData']
        let fieldsMul = ['EducationData', 'ExperienceData', 'ReferenceData']
        let langField = ['LanguageData', 'TechLanguageData',]
        for (let i = 0; i < Data.length; i++) {
            Object.keys(Data[i][fields[i]]).forEach(item => {
                try {
                    if (item == 'state_id') {
                        document.getElementById('id_state').value = Data[i][fields[i]][item]
                    }
                    else if (item == 'city') {
                        getcity(Data[i][fields[i]][item])

                    }
                    else {
                        document.getElementById(`id_${item}`).value = Data[i][fields[i]][item]
                    }
                }
                catch { }
            });
        }

        TechLanguageData1 = Languages[1]['TechLanguageData']
        let techLang = document.getElementsByName('techLanguage')
        TechLanguageData1.forEach(TechLanguageData => {
            techLang.forEach(element => {
                if (element.value == TechLanguageData['techLanguage_id']) {
                    element.checked = true
                    document.getElementById(TechLanguageData['techLangExpertise'] + '_' + TechLanguageData['techLanguage_id']).checked = true
                }
            });
        });
        LanguageData1 = Languages[0]['LanguageData']
        let lang = document.getElementsByName('language')

        LanguageData1.forEach(LanguageData => {
            lang.forEach(element => {
                if (element.value == LanguageData['language_id']) {
                    element.checked = true
                    expertiseData = String(LanguageData['expertise']).split(',')
                    for (i = 0; i < expertiseData.length - 1; i++) {
                        document.getElementById(expertiseData[i] + '_' + LanguageData['language_id']).checked = true
                    }
                }
            });
        });
        let Education = MultiData[0]['EducationData']
        for (let i = 1; i < Education.length; i++) {
            AddForm(i, 'EducationForm')
        }
        let AllBoard = document.getElementsByName('board_name')
        let AllPassYear = document.getElementsByName('passing_year')
        let percentage = document.getElementsByName('percentage')
        for (let i = 0; i < AllBoard.length; i++) {
            AllBoard[i].value = Education[i]['board_name']
            AllPassYear[i].value = Education[i]['passing_year']
            percentage[i].value = Education[i]['percentage']
        }

        let Experience = MultiData[1]['ExperienceData']
        for (let i = 1; i < Experience.length; i++) {
            AddForm(i, 'ExperienceForm')
        }
        let Allcompany = document.getElementsByName('company_name')
        let ex_designation = document.getElementsByName('ex_designation')
        let from_date = document.getElementsByName('from_date')
        let to_date = document.getElementsByName('to_date')
        for (let i = 0; i < Allcompany.length; i++) {
            Allcompany[i].value = Experience[i]['company_name']
            ex_designation[i].value = Experience[i]['ex_designation']
            from_date[i].value = Experience[i]['from_date']
            to_date[i].value = Experience[i]['to_date']
        }

        let Reference = MultiData[2]['ReferenceData']
        for (let i = 1; i < Reference.length; i++) {
            AddForm(i, 'ReferenceForm')
        }
        let AllName = document.getElementsByName('ref_name')
        let Conatcts = document.getElementsByName('ref_contact')
        let Relations = document.getElementsByName('ref_relation')
        for (let i = 0; i < AllName.length; i++) {
            AllName[i].value = Reference[i]['ref_name']
            Conatcts[i].value = Reference[i]['ref_contact']
            Relations[i].value = Reference[i]['ref_relation']
        }
    }

}

var c = document.getElementById('Languages').getElementsByTagName('input');
for (var i = 0; i < c.length; i++) {
    if (c[i].type == 'checkbox' || 'radio') {
        c[i].addEventListener('click', checkboxChecked)
        if (location.href == 'http://127.0.0.1:8000/job/') {
            c[i].click();
            c[i].click();
        }
    }
}
function checkboxChecked() {
    element = this
    if (element.checked == true) {
        try {
            document.getElementById(`Beginner_${element.value}`).disabled = false;
            document.getElementById(`Mediator_${element.value}`).disabled = false;
            document.getElementById(`Expert_${element.value}`).disabled = false;
        }
        catch { }
        try {
            document.getElementById(`read_${element.value}`).disabled = false;
            document.getElementById(`write_${element.value}`).disabled = false;
            document.getElementById(`speak_${element.value}`).disabled = false;
        }
        catch { }
    }
    else {
        try {
            document.getElementById(`Beginner_${element.value}`).disabled = true;
            document.getElementById(`Mediator_${element.value}`).disabled = true;
            document.getElementById(`Expert_${element.value}`).disabled = true;

            document.getElementById(`Beginner_${element.value}`).checked = false;
            document.getElementById(`Mediator_${element.value}`).checked = false;
            document.getElementById(`Expert_${element.value}`).checked = false;
        }
        catch { }
        try {
            document.getElementById(`read_${element.value}`).disabled = true;
            document.getElementById(`write_${element.value}`).disabled = true;
            document.getElementById(`speak_${element.value}`).disabled = true;


            document.getElementById(`read_${element.value}`).checked = false;
            document.getElementById(`write_${element.value}`).checked = false;
            document.getElementById(`speak_${element.value}`).checked = false;
        }
        catch { }
    }
}
let stateElement = document.getElementById('id_state')
stateElement.addEventListener('change', getcity)
let citySelect = document.getElementById('id_city')


async function getcity(value1) {
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
                if (typeof (value1) !== 'object') {
                    document.getElementById('id_city').value = value1
                }
            })

    }
    else {
        citySelect.innerHTML = '<option>---------</option>'
    }
}

function AddForm(btn, FormID) {
    let btn_id = btn;
    let myform = document.getElementById(FormID)
    let node = myform.querySelector('.table')
    const clone = node.cloneNode(true);
    let Removebtn = clone.querySelector('li');
    clone.id = `${FormID}_${Number(btn_id) + 1}`

    let inputsAll = clone.querySelectorAll('input')

    for (let i = 0; i < inputsAll.length; i++) {
        const element = inputsAll[i];
        element.addEventListener('keyup', DataChanged)

    }
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
    node = document.getElementById(`${FormID.id}_${btn_id}`)
    node.remove()
}


let inputTags = document.getElementsByTagName('input')
var address = document.getElementById('id_address')
address.removeAttribute('required')
address.addEventListener('keyup', DataChanged)
for (let j = 2; j < inputTags.length; j++) {
    inputTags[j].removeAttribute('required')
    inputTags[j].addEventListener('keyup', DataChanged)
}

let selectTags = document.getElementsByTagName('select')
for (let i = 0; i < selectTags.length; i++) {
    selectTags[i].addEventListener('change', DataChanged)
    selectTags[i].removeAttribute('required')
}

var isValid = []

function DataChanged(e) {
    element = e.target;
    if (element.name == 'address' && element.value.length <= 15) {
        document.getElementById('address_error').innerHTML = 'address should be at least 15 charachter'
        isValid.push(element.name)
    }
    else {
        document.getElementById('address_error').innerHTML = ''
    }
    if (element.name == 'firstname' || element.name == 'lastname' || element.name == 'designation' || element.name == 'board_name' || element.name == 'company_name' || element.name == 'ex_designation' || element.name == 'ref_name' || element.name == 'ref_relation') {
        if ((element.value).length < 3) {
            document.getElementById(element.name + '_error').innerHTML = 'field requred at least 4 charachter'
            isValid.push(element.name)
        } else {
            document.getElementById(element.name + '_error').innerHTML = ''
        }
    }
    if (element.name == 'email') {
        var validRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if (!element.value.match(validRegex)) {
            document.getElementById(element.name + '_error').innerHTML = 'enter valid email'
            isValid.push(element.name)
        }
        else {
            document.getElementById(element.name + '_error').innerHTML = ''
        }
    }
    if (element.name == 'gender' || element.name == 'relationship_status' || element.name == 'state' || element.name == 'city' || element.name == 'pref_loaction' || element.name == 'pref_department') {
        if (element.value == '') {
            document.getElementById(`${element.name}_error`).innerHTML = `${element.name} field is requred`
            isValid.push(element.name)
        }
        else {
            document.getElementById(`${element.name}_error`).innerHTML = ''
        }
    }

    if (element.name == 'phone' || element.name == 'ref_contact') {
        if ((element.value).length < 10 || (element.value).length > 10) {
            document.getElementById(element.name + '_error').innerHTML = 'enter valid phone number with 10 numerical charachter'
            isValid.push(element.name)
        } else {
            document.getElementById(element.name + '_error').innerHTML = ''
        }
    }
    if (element.name == 'dob') {
        let date = new Date()
        a = new Date(element.value)
        if (date < a) {
            document.getElementById('dob_error').innerHTML = 'you can\'t select future date'
            isValid.push(element.name)
        }
        else if (new Date('1949-12-31') > a) {
            document.getElementById('dob_error').innerHTML = 'can\'t select date before 01-01-1950'
            isValid.push(element.name)
        }
        else if (element.value == '') {
            document.getElementById(element.name + '_error').innerHTML = 'Date of birth Required'
        }
        else {
            document.getElementById('dob_error').innerHTML = ''
        }

    }
    if (element.name == 'zipcode') {
        if (element.value.length < 5) {
            document.getElementById(element.name + '_error').innerHTML = 'Enter valid zipcode'
            isValid.push(element.name)
        }
        else {
            document.getElementById(element.name + '_error').innerHTML = ''
        }
    }

    if (element.name == 'passing_year') {
        if (element.value < 2000) {
            document.getElementById(element.name + '_error').innerHTML = 'Can\'t select year before 2000'
            isValid.push(element.name)
        }
        else if (new Date().getFullYear() < element.value) {
            document.getElementById(element.name + '_error').innerHTML = 'Can\'t select future year'
            isValid.push(element.name)
        }
        else {
            document.getElementById(element.name + '_error').innerHTML = ''
        }
    }
    if (element.name == 'percentage') {
        if (element.value <= 0) {
            document.getElementById(element.name + '_error').innerHTML = 'Percentage can\'t be less than or equal to  zero'
            isValid.push(element.name)
        }
        else if (element.value > 100) {
            document.getElementById(element.name + '_error').innerHTML = 'Percentage can\'t be greter than 100'
            isValid.push(element.name)
        }
        else {
            document.getElementById(element.name + '_error').innerHTML = ''
        }
    }

    if (element.name == 'from_date' || element.name == 'to_date') {

        let from_date = document.getElementById('id_from_date')
        let to_date = document.getElementById('id_to_date')

        if (new Date(element.value).getFullYear() < 2000) {
            document.getElementById(element.name + '_error').innerHTML = 'Can\'t select year before 2000'
            isValid.push(element.name)
        }
        else if (new Date().getFullYear() < new Date(element.value).getFullYear()) {
            document.getElementById(element.name + '_error').innerHTML = 'Can\'t select future year'
            isValid.push(ele45ent.name)
        }
        else if (new Date(to_date.value).getTime() === new Date(from_date.value).getTime()) {
            document.getElementById(element.name + '_error').innerHTML = 'To date can\'t be equal to from date'
            isValid.push(element.name)
        }
        else if (element.value == '') {
            document.getElementById(element.name + '_error').innerHTML = 'Date Required'
        }
        else {
            document.getElementById(element.name + '_error').innerHTML = ''
        }
    }

    if (element.name == 'notice_period') {
        if (element.value == 0 || element.value > 10) {
            document.getElementById(element.name + '_error').innerHTML = `Notice period can\'t be ${element.value == '' ? 'Empty' : element.value + ' months'}`
            isValid.push(element.name)
        }
        else {
            document.getElementById(element.name + '_error').innerHTML = ''
        }
    }
    if (element.name == 'expected_ctc' || element.name == 'current_ctc') {
        if (element.value == 0) {
            document.getElementById(element.name + '_error').innerHTML = element.name + ' can\'t be zero'
            isValid.push(element.name)
        }
        else {
            document.getElementById(element.name + '_error').innerHTML = ''
        }
    }

}

function validateThePage() {
    if (document.getElementById('id_city').value == '---------') {
        document.getElementById('city_error').innerHTML = 'City can\'t be blank'
        return false
    }
    AllLanguages = document.getElementsByName('language')
    expertiseValue = ['read', 'write', 'speak']
    selectedLanguage = 0
    for (let i = 0; i < AllLanguages.length; i++) {
        const element = AllLanguages[i];
        a = []
        expertiseValue.filter(item => {
            if (document.getElementById(`${item}_${element.value}`).checked == 1) {
                a.push(true)
            }
        })
        if (a.length == 0 && element.checked == 1) {
            element.click()
        }
        else if (a.length > 0 && element.checked == 1) {
            selectedLanguage += 1
        }
    }
    AllTechLanguages = document.getElementsByName('techLanguage')
    expertiseValue = ['Beginner', 'Mediator', 'Expert']
    selectedTechLanguage = 0
    for (let i = 0; i < AllTechLanguages.length; i++) {
        const element = AllTechLanguages[i];
        a = []
        expertiseValue.filter(item => {
            if (document.getElementById(`${item}_${element.value}`).checked == 1) {
                a.push(true)
            }
        })
        if (a.length == 0 && element.checked == 1) {
            element.click()
        }
        else if (a.length > 0 && element.checked == 1) {
            selectedTechLanguage += 1
        }
    }
    if (selectedLanguage == 0) {
        document.getElementById('language_error').innerHTML = "At Least 1 Language Requred"

    }
    else {
        document.getElementById('language_error').innerHTML = ""

    }
    if (selectedTechLanguage == 0) {
        document.getElementById('techLanguage_error').innerHTML = "At Least 1 Tech Language Requred"
    }
    else {
        document.getElementById('techLanguage_error').innerHTML = ""
    }
    isValid = []
    Object.keys(inputTags).map((j) => {
        triggerEvent(inputTags[j], 'keyup', 13)
    });
    triggerEvent(address, 'keyup', 13)
    let selectTags = document.getElementsByTagName('select')
    for (let i = 0; i < selectTags.length; i++) {
        selectCheck(selectTags[i])
    }
    if (selectedLanguage > 0 && selectedTechLanguage > 0) {
        return isValid.length == 0 ? true : false
    }
    return false
}

function triggerEvent(el, type, keyCode) {
    if ('createEvent' in document) {
        // modern browsers, IE9+
        var e = document.createEvent('HTMLEvents');
        e.keyCode = keyCode;
        e.initEvent(type, false, true);
        el.dispatchEvent(e);
    }
    else {
        // IE 8
        var e = document.createEventObject();
        e.keyCode = keyCode;
        e.eventType = type;
        el.fireEvent('on' + e.eventType, e);
    }
}


function selectCheck(element) {
    console.log(element.name);
    if (element.value == '') {
        document.getElementById(`${element.name}_error`).innerHTML = `${element.name} field is requred`
        isValid.push(element.name)
    }
    else {
        document.getElementById(`${element.name}_error`).innerHTML = ''
    }
}