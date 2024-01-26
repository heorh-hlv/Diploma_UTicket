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