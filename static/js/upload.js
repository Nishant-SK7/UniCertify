function openModal() {
  document.getElementById("uploadModal").style.display = "block";
}
function closeModal() {
  document.getElementById("uploadModal").style.display = "none";
}
// Close modal if user clicks outside
window.onclick = function(event) {
  let modal = document.getElementById("uploadModal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

