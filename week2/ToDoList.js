var myNodelist = document.getElementsByTagName("LI");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var button = document.createElement("img");
  button.setAttribute("src","delete.jpg");
  button.className = "close";
  myNodelist[i].appendChild(button);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
  }
}, false);


function newElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("newbtn").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("You must write something!");
  } else {
    document.getElementById("list").appendChild(li);
  }
  document.getElementById("newbtn").value = "";

  var button = document.createElement("img");
  button.setAttribute("src", "delete.jpg")
  button.className = "close";
  li.appendChild(button);

  var button = document.createElement("input");
  button.setAttribute("type", "checkbox");
  button.className = "add";
  li.appendChild(button);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}

