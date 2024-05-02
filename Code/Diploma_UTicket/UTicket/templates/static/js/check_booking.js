const showTicketForm = document.getElementById('ticket_number').closest('form');
const ticketData = document.getElementById('ticket-data');
showTicketForm.addEventListener('submit', (e) => {
   e.preventDefault()
   if (!isFormFilled) return;
   ticketData.classList.remove('hidden');
})