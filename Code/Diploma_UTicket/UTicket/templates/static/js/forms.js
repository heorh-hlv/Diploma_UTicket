//todo INPUT SHOW/HIDE PASSWORD
const showHidePwdButtons = document.querySelectorAll('#show-hide-password');
showHidePwdButtons.forEach(showHidePwdButton => {
   showHidePwdButton.addEventListener('click', showHidePassword);
})
function showHidePassword() {
   let input = this.parentElement.querySelector('#input-password'),
      eyeClosed = this.querySelector('.eye-closed'),
      eyeOpened = this.querySelector('.eye-opened');
   if (input.type == 'password') {
      input.type = 'text'
   } else if (input.type == 'text') {
      input.type = 'password'
   }
   eyeOpened.classList.toggle('hidden');
   eyeClosed.classList.toggle('hidden');
}

//? limit max date in input[type='date'] for birthday
const inputsBirthday = document.querySelectorAll('.input-birthday')
inputsBirthday.forEach(inputBirthday => {
   inputBirthday.max = new Date().toISOString().split('T')[0];
})



//todo DROPDOWN MENU
const dropdowns = document.querySelectorAll(".wrapper-dropdown");

//? open all the dropdowns
function handleDropdown(dropdown, toOpen) {
   if (toOpen) {
      dropdown.classList.add("active");
   } else {
      dropdown.classList.remove("active");
   }
}

//? close all the dropdowns
function closeAllDropdowns() {
   const dropdowns = document.querySelectorAll(".wrapper-dropdown");
   dropdowns.forEach((dropdown) => {
      handleDropdown(dropdown, false);
   });
}
dropdowns.forEach((dropdown) => {
   const optionsList = dropdown.querySelectorAll("div.wrapper-dropdown li");
   const dropdownInput = dropdown.querySelector('input')
   dropdown.addEventListener("click", () => {
      if (dropdown.classList.contains("active")) {
         handleDropdown(dropdown, false);
      } else {
         let currentActive = document.querySelector(".wrapper-dropdown.active");
         if (currentActive) {
            handleDropdown(currentActive, false);
         }
         handleDropdown(dropdown, true);
      }
   });

   //? update the display of the dropdown
   for (let option of optionsList) {
      option.addEventListener("click", () => {
         dropdown.querySelector(".selected-display").innerHTML = option.innerHTML;
         dropdownInput.value = option.textContent;
         formField = dropdownInput.closest('.field')
         formField.blur();
      });
   }
});

//? check if anything else other than the dropdown is clicked
window.addEventListener("click", function (e) {
   if (!e.target.closest(".wrapper-dropdown")) {
      closeAllDropdowns();
   }
});



//todo Validation for forms
var isFormFilled = false
const form = document.querySelector('.form');
console.log(form)
const fields = document.querySelectorAll('.field');
validateUnfilledForm(fields)

//? Validation form for unfilled fields
function validateUnfilledForm(formFields) {
   formFields.forEach(field => {
      if (!field.querySelector('.error')) return //? skip iteration if a field is not required (does not contain prepared error message
      const fieldError = field.querySelector('.error')
      field.addEventListener('focusout', (e) => {
         if (field.querySelector('input').value === '') {
            fieldError.classList.remove('hidden')
            fieldError.classList.add('show')
         } else if (fieldError.innerText === 'Це поле має бути заповнене.') {
            fieldError.classList.add('hidden')
            fieldError.classList.remove('show')
         }
      })
   })
}
if (form) {
form.addEventListener('submit', (e) => {
   fields.forEach(field => {
      if (!field.querySelector('.error')) return
      const fieldError = field.querySelector('.error')
      if (field.querySelector('input').value === '') {
         fieldError.classList.remove('hidden')
         fieldError.classList.add('show')
      } else if (fieldError.innerText === 'Це поле має бути заповнене.') {
         fieldError.classList.add('hidden')
         fieldError.classList.remove('show')
      }
   })
   if (form.querySelector('.error.show')) {
      isFormFilled = false;
   } else {
      isFormFilled = true;
   }
   if (!isFormFilled) {
      e.preventDefault()
      if (form.querySelector('.error.show').closest('.form-chapter')) {
         scrollTo({
            top: form.querySelector('.error.show').closest('.form-chapter').offsetTop,
            left: 0,
            behavior: 'smooth'
         })
      }
   }
})
}



//? validate cities
const dropdownDepartureCity = document.querySelector('input#city-of-departure') ? document.querySelector('input#city-of-departure').closest('.wrapper-dropdown') : null;
const dropdownDestinationCity = document.querySelector('input#city-destination') ? document.querySelector('input#city-destination').closest('.wrapper-dropdown') : null;
var chosenCity = '';

//? disable Destination City dropdown menu before departure city is chosen
if (dropdownDepartureCity && dropdownDestinationCity) {
   dropdownDestinationCity.classList.add('disable');
   const departureCityOptionsList = dropdownDepartureCity.querySelectorAll("li");
   const destinationCityOptionsList = dropdownDestinationCity.querySelectorAll("li");

   //? update the display of the dropdown
   for (let option of departureCityOptionsList) {
      option.addEventListener("click", () => {
         chosenCity = option.innerHTML;
         destinationCityOptionsList.forEach(city => {
            if (city.innerHTML === chosenCity) {
               city.classList.add('hidden')
            } else {
               city.classList.remove('hidden')
            }
         })
         dropdownDestinationCity.querySelector('#destination').innerHTML = 'Не обрано';
         dropdownDestinationCity.querySelector('input').value = '';
         dropdownDestinationCity.classList.remove('disable');
      });
   }
}

////? validate dates
const returnDateInput = document.getElementById('return_date')
const departureDateInput = document.getElementById('departure_date')
if (returnDateInput) {
    if (departureDateInput) {
        departureDateInput.value = '';
        returnDateInput.value = '';
        var chosenDepartureDate = '';

        //? disable returnDateInput  before departure date is chosen
        returnDateInput.classList.add('disable');

        //? set the minimum departure date to current date
        departureDateInput.min = new Date().toISOString().split('T')[0];
        departureDateInput.max = getDateAfterNYearsFromDate(new Date(), 1);

        departureDateInput.addEventListener('change', () => {
          returnDateInput.classList.remove('disable');
          returnDateInput.value = '';
          returnDateInput.min = departureDateInput.value;
          returnDateInput.max = getDateAfterNYearsFromDate(new Date(departureDateInput.value), 1);;
        })
    }

}
else {
    if (departureDateInput ) {
        departureDateInput.value = '';
        var chosenDepartureDate = '';

        //? set the minimum departure date to current date
        departureDateInput.min = new Date().toISOString().split('T')[0];
        departureDateInput.max = getDateAfterNYearsFromDate(new Date(), 1);
    }
}


function getDateAfterNYearsFromDate(inputDate, n) {
   if (typeof n !== 'number' || n < 0) {
      throw new Error('Invalid input for the number of years. Please provide a positive number of years.');
   }
   if (!(inputDate instanceof Date)) {
      throw new Error('Invalid input date. Please provide a valid Date object.');
   }
   //? create a copy of the input date
   const dateCopy = new Date(inputDate);

   //? add n years to the copied date
   dateCopy.setFullYear(dateCopy.getFullYear() + n);

   //? extract year, month, and day components
   const year = dateCopy.getFullYear();
   const month = (dateCopy.getMonth() + 1).toString().padStart(2, '0');
   const day = dateCopy.getDate().toString().padStart(2, '0');

   //? format the date as "yyyy-mm-dd"
   const formattedDate = `${year}-${month}-${day}`;

   return formattedDate;
}


//? validate ticket id for booking cancelling
const ticketIdRegex = /^.{10}$/;
const ticketIdInput = document.getElementById('ticket_number')
if (ticketIdInput) {
   ticketIdInput.addEventListener('focusout', (e) => {
      let enteredTicketId = e.target.value;
      const fieldError = e.target.parentElement.parentElement.querySelector('#form-field-error')
      if (!ticketIdRegex.test(enteredTicketId) && enteredTicketId) {
         fieldError.innerText = 'Невалідний формат.';
         fieldError.classList.remove('hidden')
         fieldError.classList.add('show')
      } else {
         fieldError.innerText = 'Це поле має бути заповнене.';
         fieldError.classList.add('hidden')
         fieldError.classList.remove('show')
      }
   })
}



// Formatting and validation for card number input
const cardNumberInput = document.querySelector('#id_card_number');
console.log(cardNumberInput)

if (cardNumberInput) {
    cardNumberInput.addEventListener('input', () => {
        let input = cardNumberInput.value.replace(/\D/g, '').substring(0, 16); // Keep only digits, max length 16
        let formattedInput = '';
        for (let i = 0; i < input.length; i++) {
            if (i > 0 && i % 4 === 0) {
                formattedInput += ' ';
            }
            formattedInput += input[i];
        }
        cardNumberInput.value = formattedInput;
    });

    cardNumberInput.addEventListener('blur', () => {
        const fieldError = cardNumberInput.parentElement.querySelector('.error');
        if (!/^\d{4} \d{4} \d{4} \d{4}$/.test(cardNumberInput.value)) {
            fieldError.classList.remove('hidden');
            fieldError.classList.add('show');
        } else {
            fieldError.classList.add('hidden');
            fieldError.classList.remove('show');
        }
    });
}

// Validation for expiry date input
const cardExpiryInput = document.getElementById('id_card_expiry');
if (cardExpiryInput) {
    cardExpiryInput.addEventListener('input', () => {
        let input = cardExpiryInput.value.replace(/\D/g, '').substring(0, 4); // Keep only digits, max length 4
        let formattedInput = '';
        if (input.length >= 2) {
            formattedInput = input.substring(0, 2) + '/' + input.substring(2, 4);
        } else {
            formattedInput = input;
        }
        cardExpiryInput.value = formattedInput;
    });

    cardExpiryInput.addEventListener('blur', () => {
        validateExpiryDate();
    });
}

function validateExpiryDate() {
    const fieldError = cardExpiryInput.parentElement.querySelector('.error');
    if (!/^(0[1-9]|1[0-2])\/?([0-9]{2})$/.test(cardExpiryInput.value)) {
        fieldError.innerText = 'Невалідний формат.';
        fieldError.classList.remove('hidden');
        fieldError.classList.add('show');
        return false;
    } else {
        fieldError.classList.add('hidden');
        fieldError.classList.remove('show');
        return true;
    }
}

document.querySelector('form').addEventListener('submit', (event) => {
    if (!validateExpiryDate()) {
        event.preventDefault();
    }
});


// Validation for CVV input
document.querySelector('form').addEventListener('submit', (event) => {
    if (!validateExpiryDate() || !validateCVV()) {
        event.preventDefault();
    }
});
const cardCvvInput = document.getElementById('id_card_cvv');
if (cardCvvInput) {
    cardCvvInput.addEventListener('input', () => {
        console.log("CVV input event triggered");
        cardCvvInput.value = cardCvvInput.value.replace(/\D/g, '').substring(0, 3); // Keep only digits, max length 3
    });

    cardCvvInput.addEventListener('blur', () => {
        validateCVV();
    });
}

function validateCVV() {
    const cardCvvInput = document.getElementById('id_card_cvv');
    const fieldError = cardCvvInput.parentElement.querySelector('.error');
    if (!/^\d{3}$/.test(cardCvvInput.value)) {
        fieldError.classList.remove('hidden');
        fieldError.classList.add('show');
        return false;
    } else {
        fieldError.classList.add('hidden');
        fieldError.classList.remove('show');
        return true;
    }
}






//todo other-reasons-textearea triggering
const radioButtons = document.querySelectorAll('input[type="radio"][name="cancel-reason"]');
const otherReasonsTextarea = document.getElementById('other-reasons-cancelling-textarea');
if (radioButtons && otherReasonsTextarea) {
   if (document.getElementById('other-reasons-cancelling-trigger').checked) {
      otherReasonsTextarea.classList.remove('hidden');
   } else {
      otherReasonsTextarea.classList.add('hidden');
   }
   radioButtons.forEach(radio => {
      radio.addEventListener('click', () => {
         if (radio.id === 'other-reasons-cancelling-trigger' && radio.checked) {
            otherReasonsTextarea.classList.remove('hidden');
         } else {
            otherReasonsTextarea.classList.add('hidden');
         }
      });
   });
}



//todo chars counter
var charsCounters = document.querySelectorAll('.chars-counter');
charsCounters.forEach(charsCounter => {
   const countedCharsArea = charsCounter.parentElement.querySelector('.counted-chars-area');
   const maxChars = countedCharsArea.maxLength;
   countedCharsArea.addEventListener('input', () => {
      inputChars = countedCharsArea.value.length;
      charsCounter.textContent = inputChars + ' / ' + maxChars;
   })
})

