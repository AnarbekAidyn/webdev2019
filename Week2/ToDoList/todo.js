function  Tasks(){
  var val=document.getElementById('input').value;
  var txt = document.createTextNode(val);
  var li=document.createElement('li');
  var checking=document.createElement("INPUT");
  checking.type="checkbox";
  checking.className="checkclass";
  li.append(checking);
  li.append(txt);
  
  if(val==="" || val===" "){
      alert('Please, write something');
  }
  else {
      document.getElementById('myList').append(li);
  }

  document.getElementById('input').value="";
  var btn = document.createElement("INPUT");
  btn.className="close";
  btn.value="delete";
  btn.type="button";
  li.appendChild(btn);
  li.onclick=fnctnOnItem;
}
function fnctnOnItem(e){
    if(e.target.className==="close"){
        var div=e.target.parentNode;
        div.remove();
    }
    else if(e.target.className==="checkclass"){
        e.target.parentNode.classList.toggle('checked');
    }

}