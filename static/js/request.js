
  function openRequestModal() {
    document.getElementById("requestModal").style.display = "block";
  }
  function closeRequestModal() {
    document.getElementById("requestModal").style.display = "none";
  }
  window.onclick = function(event) {
    let modal = document.getElementById("requestModal");
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
