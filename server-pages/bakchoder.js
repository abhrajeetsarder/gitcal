var request = new Request('https://api.ipify.org/?format=');
fetch(request).then(function(response) {
  return response.text();
}).then(function(text) {
  resp = text.substring(0, 30);
  document.getElementById('ipaddress').innerHTML = "Yeah, Your IP address is "+resp;
});

function disableClick(){
    document.onclick=function(event){
      if (event.button == 2) {
        alert('Right Click Message');
        return false;
      }
    }
}

function validateForm() {
  var x = document.forms["myForm"]["inputs"].value;
  if (x == "") {
    alert("Enter A Value to Calculate!");
    return false;
  }
}

function callbackReturn(hell){
  element = document.getElementById('value').value
  key = event.key
  if(/^[+()/*\d-]+$/.test(key)){
    if(key == '*'){
      hell.value = element+"X";
    }
    
    else if(key == "/"){
      hell.value = element+"÷";
    }
    else{
      hell.value = element+key;
    }
  }
  else if(event.key == 'Backspace' || event.key == 'Delete'){
    str = document.getElementById('value').value;
    str = str.slice(0, str.length - 1);
    document.getElementById('value').value = str;
  }
  else{
    
  }
}

function callbackReturn2(hell){
  
  key = event.key
  alert(key)
}

  function onClickFunction(val){
    var inp = val.value;
    if(inp === '⌫'){
        str = document.getElementById('value').value;
        str = str.slice(0, str.length - 1);
        document.getElementById('value').value = str;
    }
    else if(inp === 'CL'){
        document.getElementById('value').value = "";
    }
    else if(document.getElementById('value').value != null){
        var valu = document.getElementById('value').value;
        document.getElementById('value').value = valu+inp;
    }
  }  