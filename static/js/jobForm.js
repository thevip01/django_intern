inputTags = document.getElementsByTagName('input')
address = document.getElementById('id_address')
address.addEventListener('keyup', DataChanged)

for (let j = 2; j < inputTags.length; j++) {
    inputTags[j].addEventListener('keyup', DataChanged)
}

selectTags = document.getElementsByTagName('select')
for (let i = 0; i < selectTags.length; i++) {
    selectTags[i].addEventListener('change', DataChanged)
}

isValid = []

function DataChanged(e) {
    element = e.target

    console.log((element.name).substring(0, length(element.name) - 1));
    debugger
    if (element.name == 'address' && element.value.length <= 15) {
        document.getElementById('address_error').innerHTML = 'address should be at least 15 charachter'
        isValid.push(element.name)
    }
    else {
        document.getElementById('address_error').innerHTML = ''
    }
    if (element.name == 'firstname' || element.name == 'lastname' || element.name == 'designation' || element.name == 'company_name' || element.name == 'ex_designation' || element.name == 'ref_name' || element.name == 'ref_relation') {
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
        console.log(element.value);
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
            console.log(element.name);
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
        if (element.value < 2000) {
            document.getElementById(element.name + '_error').innerHTML = 'Can\'t select year before 2000'
            isValid.push(element.name)
        }
        else if (new Date().getFullYear() < element.value) {
            document.getElementById(element.name + '_error').innerHTML = 'Can\'t select future year'
            isValid.push(element.name)
        }
        else if (new Date(to_date.value) < new Date(from_date.value)) {
            document.getElementById(element.name + '_error').innerHTML = 'To date can\'t be less than from date'
            isValid.push(element.name)
        }
        else if (new Date(to_date.value).getTime() === new Date(from_date.value).getTime()) {
            document.getElementById(element.name + '_error').innerHTML = 'To date can\'t be equal to from date'
            isValid.push(element.name)
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
    isValid = []
    Object.keys(inputTags).map((j) => {
        triggerEvent(inputTags[j], 'keyup', 13)
    });
    console.log(isValid);
    return isValid.length == 0 ? true : false
}

function triggerEvent(el, type, keyCode) {
    if ('createEvent' in document) {
        // modern browsers, IE9+
        var e = document.createEvent('HTMLEvents');
        e.keyCode = keyCode;
        e.initEvent(type, false, true);
        el.dispatchEvent(e);
    } else {
        // IE 8
        var e = document.createEventObject();
        e.keyCode = keyCode;
        e.eventType = type;
        el.fireEvent('on' + e.eventType, e);
    }
}