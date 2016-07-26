var sock = new SockJS('http://localhost:6543/__sockjs__');

sock.onopen = function() {
  console.log('open');
};

sock.onmessage = function(obj) {
  console.log(obj);
};

sock.onclose = function() {
  console.log('close');
};

