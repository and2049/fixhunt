(function(){ var f = () => {}; console.log('unwrapped:', typeof f); })();
(function(){ var f = () => {}; console.log('wrapped:', typeof f()); })();
