function leftTimer(year,month,day,hour,minute,second){
  let leftTime = (new Date(year,month-1,day,hour,minute,second)) - (new Date());
  let days = parseInt(leftTime / 1000 / 60 / 60 / 24 , 10); 
  let hours = parseInt(leftTime / 1000 / 60 / 60 % 24 , 10);  
  let minutes = parseInt(leftTime / 1000 / 60 % 60, 10);
  let seconds = parseInt(leftTime / 1000 % 60, 10);
  days = checkTime(days); 
  hours = checkTime(hours); 
  minutes = checkTime(minutes); 
  seconds = checkTime(seconds); 
  document.getElementById("timer").innerHTML = days+" 天 " + hours+" 小时 " + minutes+" 分 "+seconds+" 秒 ";  
} 

function checkTime(i){ 
  if(i<10) 
  { 
    i = "0" + i; 
  } 
  return i; 
}