//todo POPUP FORMS
const popupSingup = document.getElementById('signup-form');
const popupLogin = document.getElementById('login-form');
const showSingupButton = document.getElementById('signup-trigger');
const showLoginButton = document.getElementById('login-trigger');
const closeButtons = document.querySelectorAll('#close-form');

function openPopupSignup() {
   popupLogin.classList.remove('show-form');
   popupSingup.classList.add('show-form');
   document.body.classList.add('body-blocked');
}
function openPopupLogin() {
   popupSingup.classList.remove('show-form');
   popupLogin.classList.add('show-form');
   document.body.classList.add('body-blocked');
}

showSingupButton.addEventListener('click', openPopupSignup)
showLoginButton.addEventListener('click', openPopupLogin)

closeButtons.forEach(closeButton => {
   closeButton.addEventListener('click', (e) => {
      e.target.closest('.pop-up__log-form').classList.remove('show-form');
      document.body.classList.remove('body-blocked');
   })
})
document.addEventListener('click', (e) => {
   if (e.target.closest('.background-darken')) {
      e.target.closest('.pop-up__log-form').classList.remove('show-form');
      document.body.classList.remove('body-blocked');
   }
})




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




//todo BURGER MENU
const menu = document.getElementById('menu')
const openMenu = document.getElementById('open-menu')
const closeMenu = document.getElementById('close-menu')

openMenu.addEventListener('click', () => {
   menu.classList.add('show-menu')
})
closeMenu.addEventListener('click', () => {
   menu.classList.remove('show-menu')
})
document.addEventListener('click', (e) => {
   if (!e.target.closest('.show-menu') && !e.target.closest('.open-menu')) {
      menu.classList.remove('show-menu')
   }
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
   console.log(dropdownInput)

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
         formField = dropdownInput.closest('.chapter__field')
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
const chapterFields = document.querySelectorAll('.chapter__field');

validateUnfilledForm(chapterFields)

//? Validation form for unfilled fields
function validateUnfilledForm(formFields) {
   formFields.forEach(field => {
      if (!field.querySelector('#form-field-error')) { //? skip iteration if a field is not required (does not contain prepared error message)
         return
      }
      const fieldError = field.querySelector('#form-field-error')
      field.addEventListener('focusout', (e) => {
         if (field.querySelector('input').value === '') {
            fieldError.classList.remove('hidden')
            fieldError.classList.add('show')
         } else if (fieldError.innerText === 'Це поле має бути заповнене.') {
            fieldError.classList.add('hidden')
            fieldError.classList.remove('show')
         }

         console.log('isFormFilled', isFormFilled)
      })
   })
}


form.addEventListener('submit', (e) => {
   chapterFields.forEach(field => {
      if (!field.querySelector('#form-field-error')) {
         return
      }
      const fieldError = field.querySelector('#form-field-error')
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
      scrollTo({
         top: form.querySelector('.error.show').closest('.form-chapter').offsetTop,
         left: 0,
         behavior: 'smooth'
      })
   }
})


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
         console.log('chosenCity', chosenCity)
      });
   }
}

//? validate dates
const departureDateInput = document.getElementById('departure-date')
const returnDateInput = document.getElementById('return-date')

if (departureDateInput && returnDateInput) {
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


function getDateAfterNYearsFromDate(inputDate, n) {
   if (typeof n !== 'number' || n < 0) {
      throw new Error('Invalid input for the number of years. Please provide a positive number of years.');
   }

   if (!(inputDate instanceof Date)) {
      console.log(inputDate)
      throw new Error('Invalid input date. Please provide a valid Date object.');
   }

   // Create a copy of the input date
   const dateCopy = new Date(inputDate);

   // Add n years to the copied date
   dateCopy.setFullYear(dateCopy.getFullYear() + n);

   // Extract year, month, and day components
   const year = dateCopy.getFullYear();
   const month = (dateCopy.getMonth() + 1).toString().padStart(2, '0');
   const day = dateCopy.getDate().toString().padStart(2, '0');

   // Format the date as "yyyy-mm-dd"
   const formattedDate = `${year}-${month}-${day}`;

   return formattedDate;
}


//? validate the amout of passengers input
const passengersAmountInput = document.getElementById('amount-of-passengers') ? document.getElementById('amount-of-passengers') : null;

if (passengersAmountInput) {
   passengersAmountInput.addEventListener('input', (e) => {
      const inputValue = e.target.value;

      // Use a regular expression to check if the input contains anything except numbers
      const regex = /[^0-9]/g;
      const containsNonNumericCharacters = regex.test(inputValue);
      const fieldError = e.target.parentElement.parentElement.querySelector('#form-field-error')

      console.log(fieldError)

      if (containsNonNumericCharacters) {

         fieldError.innerText = 'Невалідний формат.';
         fieldError.classList.remove('hidden')
         fieldError.classList.add('show')

      } else if (inputValue > 10) {
         fieldError.innerText = 'Не більше 10 пасажирів.';
         fieldError.classList.remove('hidden')
         fieldError.classList.add('show')
      } else if (inputValue < 1) {
         fieldError.innerText = 'Не менше 1 пасажира.';
         fieldError.classList.remove('hidden')
         fieldError.classList.add('show')
      } else {
         fieldError.innerText = 'Це поле має бути заповнене.';
         fieldError.classList.add('hidden')
         fieldError.classList.remove('show')
      }

   })
}

//? validate ticket id for booking cancelling
const ticketIdRegex = /^\d{11}$/;
const ticketIdInput = document.getElementById('ticket-id')

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




//todo other reasons textearea triggering
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
const charsCounters = document.querySelectorAll('.chars-counter');

charsCounters.forEach(charsCounter => {
   const countedCharsArea = charsCounter.parentElement.querySelector('.counted-chars-area');
   const maxChars = countedCharsArea.maxLength;

   countedCharsArea.addEventListener('input', () => {
      inputChars = countedCharsArea.value.length;
      charsCounter.textContent = inputChars + ' / ' + maxChars;
   })
})