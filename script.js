let rewriteButton = document.getElementById("rewrite");

function getTextValue() {
  let textValue = document.querySelector("textarea").value;
  console.log(textValue);
}

rewriteButton.addEventListener("click", getTextValue());
