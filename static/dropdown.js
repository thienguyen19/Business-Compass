

function filterStickers() {
  const input = document.getElementById("stock_symbol");
  const dropdown = document.getElementById("stock_list");
  const filter = input.value.toUpperCase();
  const options = dropdown.getElementsByTagName("a");

  for (let i = 0; i < options.length; i++) {
    const optionText = options[i].textContent || options[i].innerText;
    if (optionText.toUpperCase().indexOf(filter) > -1) {
      options[i].style.display = "";
    } else {
      options[i].style.display = "none";
    }
  }
}

function selectSticker(option) {
  console.log("hello")
  const selectedMajor = option.textContent || option.innerText;
  
  document.getElementById("stock_symbol").value = selectedMajor;
  // Close the dropdown (optional)
  document.getElementById("stock_list").style.display = "none";
}
